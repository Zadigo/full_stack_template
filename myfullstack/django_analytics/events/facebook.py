import time

from django.conf import settings
from facebook_business.adobjects.serverside.action_source import ActionSource
from facebook_business.adobjects.serverside.content import Content
from facebook_business.adobjects.serverside.custom_data import CustomData
from facebook_business.adobjects.serverside.delivery_category import \
    DeliveryCategory
from facebook_business.adobjects.serverside.event import Event
from facebook_business.adobjects.serverside.event_request import EventRequest
from facebook_business.adobjects.serverside.user_data import UserData
from facebook_business.api import FacebookAdsApi

# https: // developers.facebook.com/docs/marketing-api/conversions-api/using-the-api  # send


class FacebookEventsInterface:
    """Helper class for sending events to 
    Facebook server side"""
    def __init__(self):
        self.access_token = getattr(settings, 'FACEBOOK_ACCESS_ID', None)
        self.pixel_id = getattr(settings, 'FACEBOOK_ADS_PIXEL_ID')
        FacebookAdsApi.init(access_token=self.access_token)

    def _build(self, request, **kwargs):
        """Sequentially build the components
        in order to send an event"""
        if request.user.is_authenticated:
            user_data = UserData(
                emails=[request.user.email],
                phones=[],
                client_ip_address=request.META.get('REMOTE_ADDR'),
                client_user_agent=request.headers['User-Agent'],
                fbc='fb.1.1554763741205.AbCdEfGhIjKlMnOpQrStUvWxYz1234567890',
                fbp='fb.1.1558571054389.1098115397',
            )

            content = Content(
                product_id=product_id,
                quantity=quantity,
                delivery_category=DeliveryCategory.HOME_DELIVERY,
            )

            custom_data = CustomData(
                contents=[content],
                currency=currency,
                value=price,
            )

            event = Event(
                event_name=event_name,
                event_time=int(time.time()),
                user_data=self.create_user_data(request),
                custom_data={},
                event_source_url=event_url,
                action_source=ActionSource.WEBSITE,
            )
        return event

    def send(self, request, **kwargs):
        new_event = self._build(request, **kwargs)
        instance = EventRequest(events=[new_event], pixel_id=self.pixel_id)
        instance.execute()
        return instance


facebook_event = FacebookEventsInterface()
