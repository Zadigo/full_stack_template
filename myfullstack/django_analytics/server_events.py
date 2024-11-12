import dataclasses
import hashlib
from collections import defaultdict

from django.conf import settings
from django.utils import timezone
from requests.models import Request
from requests.sessions import Session


@dataclasses.dataclass
class Event:
    event_name: str = None
    event_time: int = None
    action_source: str = 'website'
    event_source_url: str = None

    def __post_init__(self):
        self.event_time = timezone.now().timestamp()


class FacebookEvents:
    """
    https://developers.facebook.com/docs/marketing-api/conversions-api/payload-helper
    """
    base_url = 'https://graph.facebook.com/{api_version}/{pixel_id}/events?access_token={access_token}'
    event_class = Event

    def __init__(self, request, event_name=None, event_url=None, **context):
        self.context = context
        self.request = request
        self.event = self.event_class(
            event_name=event_name, 
            event_source_url=event_url
        )

    @staticmethod
    def hash_parameter(value):
        result = hashlib.sha256(str(value).encode('utf-8'))
        return result.hexdigest()

    def build_event_context(self):
        event_data = dataclasses.asdict(self.event)
        event_data = event_data | self.get_context()
        return {'data': [event_data]}

    def create_request(self):
        api_version = getattr(settings, 'FACEBOOK_API_VERSION', 'v20.0')
        pixel_id = getattr(settings, 'FACEBOOK_PIXEL_ID')
        access_token = getattr(settings, 'FACEBOOK_API_ACCESS_TOKEN')

        if access_token is None:
            raise ValueError()

        url = self.base_url.format(**{
            'api_version': api_version,
            'pixel_id': pixel_id,
            'access_token': access_token
        })
        print(self.build_event_context())
        request = Request(
            url=url, 
            method='post',
            json=self.build_event_context()
        )
        session = Session()
        prepared_request = session.prepare_request(request)
        return session, prepared_request

    def get_context(self, **context):
        default_context = {
            # 'client_ip_address': self.request.headers
            'client_user_agent': self.request.headers['User-Agent']
        }
        self.context['user_data'] = default_context
        return self.context | context

    def send(self):
        session, prepared_request = self.create_request()
        try:
            response = session.send(prepared_request)
        except:
            return False
        else:
            return response.json()


class ViewContent(FacebookEvents):
    def __init__(self, request, firstname=None, lastname=None, email=None, city=None, event_url=None, **context):
        super().__init__(request, event_url=event_url, **context)
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.city = city

    def get_context(self, **context):
        context = super().get_context(**context)
        params = defaultdict(list)
        params['fn'].append(self.hash_parameter(self.firstname))
        params['ln'].append(self.hash_parameter(self.lastname))
        params['em'].append(self.hash_parameter(self.email))
        params['ct'].append(self.hash_parameter(self.city))
        context['user_data'].update(**params)
        return context


# body = {
#     "data": [
#         {
#             "event_name": "ViewContent",
#             "event_time": 1727605316,
#             "action_source": "website",
#             "event_source_url": "https://gency313.fr/blog/insights/le-lexique-du-growth-marketing",
#             "user_data": {
#                 "em": [
#                     "7b17fb0bd173f625b58636fb796407c22b3d16fc78302d79f0fd30c2fc2fc068"
#                 ]
#             },
#             "custom_data": {
#                 "currency": "EUR",
#                 "value": 100
#             }
#         }
#     ]
# }

# url = 'https://graph.facebook.com/v20.0/464186372554470/events?access_token=EAAJvHcaWLeMBO1Hq2f3Up9qqqVcvalKcbZC81pXpzZA5QhVk0bDqOhhp6ZAkFH1grff2n2blhFjLbQVMblPziixMZA07jv2VyuxUCvXrVtoJ62laftPewZCEZCo5r9hObZCz8ZCTdpE3IUR9NGmPvShQZCa5ZCFZBvQ33MspdQvEkWAt0ZBNENWi3RHO58KKc7RnWE9c1AZDZD'
# request = Request(url=url, method='post', json=body)
# s = Session()
# p = s.prepare_request(request)
# r = s.send(p)
# print(r.content)
