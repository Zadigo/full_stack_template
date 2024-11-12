"""
Send server side events using the "Measurement Protocole API". For
document read the following link:

https://developers.google.com/analytics/devguides/collection/protocol/v1/devguide
"""

from urllib.parse import urlencode, urljoin

import requests

TRACKING_URL = 'https://google-analytics.com'

TRACKING_COLLECT_URL = urljoin(TRACKING_URL, 'collect')

TRACKING_DEBUG_URL = urljoin(TRACKING_URL, 'debug/collect')


class BaseProtocole:
    hit_type = None

    def __init__(self, analytics_tag, debug=False, user_id=None):
        self.is_successful = False
        self.analytics_tag = analytics_tag
        # 555 means that the user is anonymous
        # otherwise, use the actual user ID
        self.user_id = user_id or 555
        self.debug = debug
        self._final_url = None
        self.errors = []

    def __str__(self):
        return f'{self.__class__.__name__}([completed={self.is_successful}])'

    @property
    def has_errors(self):
        return len(self.errors) > 0

    def url(self):
        template = '{url}?{query}'
        if self.debug:
            result = template.format(
                url=TRACKING_DEBUG_URL,
                query=self.encoded_query()
            )
        else:
            result = template.format(
                url=TRACKING_COLLECT_URL,
                query=self.encoded_query()
            )
        self._final_url = result
        return result

    def encoded_query(self):
        return urlencode(self.query())

    def query(self, **extra_params):
        """Returns the base parameters which
        are required for event. Subclasses should
        always call this when implementing there own
        parameters

        `v`: version
        `tid`: the Google Analytics tracking ID
        `cid`: the anonymous (555) or actual user ID
        `t`: the hit type
        """
        params = {
            'v': 1,
            'tid': self.analytics_tag,
            'cid': self.user_id,
            't': self.hit_type,
            **extra_params
        }
        return params

    def send(self):
        response = requests.post(url=self.url())
        if response.status_code == 200:
            try:
                data = response.json()
            except:
                pass
            else:
                truth_array = []
                results = data['hitParsingResult']
                for result in results:
                    truth_array.append(result['valid'])
                    for message in result['parserMessage']:
                        self.errors.append(message)
                self.is_successful = all(truth_array)


class BaseEvent(BaseProtocole):
    """Base class for sending events to
    Google Analytics"""
    hit_type = 'event'
    event_category = ''
    event_action = ''
    event_label = ''
    event_value = 0

    def query(self, **extra_params):
        base_query = super().query(**extra_params)
        default_event_params = {
            'ec': self.event_category,
            'ea': self.event_action,
            'el': self.event_label,
            'ev': self.event_value
        }
        return default_event_params | base_query


class EnhancedEcommerceMixin:
    transaction_id = None
    product_action = None
    event_category = 'Ecommerce'
    non_interaction_parameter = 1


class RefundEvent(EnhancedEcommerceMixin, BaseEvent):
    event_action = 'Refund'
    product_action = 'refund'

    def __init__(self, analytics_tag, transaction_id, **kwargs):
        self.transaction_id = transaction_id
        super().__init__(analytics_tag, **kwargs)


# event = RefundEvent('G-C5VLPRS4QY', 'something_here', debug=True)
# event.send()
# print(event.has_errors)

# {
#     "hitParsingResult": [
#         {
#             "valid": false,
#             "parserMessage": [
#                 {
#                     "messageType": "ERROR",
#                     "description": "The value provided for parameter 'tid' is invalid. Please see http://goo.gl/a8d4RP#tid for details.",
#                     "messageCode": "VALUE_INVALID",
#                     "parameter": "tid"
#                 }
#             ],
#             "hit": "/debug/collect?ec=Ecommerce&ea=Refund&el=&ev=0&v=1&tid=G-C5VLPRS4QY&cid=555&t=event"
#         }
#     ],
#     "parserMessage": [
#         {
#             "messageType": "INFO",
#             "description": "Found 1 hit in the request."
#         }
#     ]
# }
