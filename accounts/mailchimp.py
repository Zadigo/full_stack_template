from typing import Union
# import mailchimp
import mailchimp_marketing as MailchimMpMarketing
from django.conf import settings
from mailchimp_marketing.api_client import ApiClientError


class Base:
    def __init__(self):
        client = MailchimMpMarketing.Client()
        client.set_config({
            'api_key': settings.MAILCHIMP_API_KEY,
            'server': settings.MAILCHIMP_SERVER
        })
        self.client = client


# Documentation: https://mailchimp.com/developer/marketing/api/list-members/get-member-info/

class Members(Base):
    def create(self, list_id: Union[int, str]):
        return self.client.lists.add_list_member()

    def associate(self, list_id: Union[int, str], email: str, status: str, **kwargs):
        authorized_status = ['subscribed', 'unsubscribed', 'cleaned', 'pending']
        if status not in authorized_status:
            raise Exception(f'Status is not valid')
        attrs = {'email': email, 'status': status}
        attrs = attrs | kwargs
        return self.client.lists.add_list_member(list_id, attrs)

    def members(self, list_id: Union[int, str]):
        return self.client.lists.get_list_member()

    def update(self, list_id: Union[int, str], subscriber_hash: str, **attrs):
        return self.client.lists.update_list_member(list_id, subscriber_hash, attrs)
