from urllib.parse import urlencode

import requests
from django.core.exceptions import ValidationError
from django.utils.crypto import get_random_string


class GetAddress:
    """Verify that an address actually exists"""
    api_url = 'https://api-adresse.data.gouv.fr/search'

    def __init__(self, addressline, zip_code=None):
        self.errors = []
        self.response = {}
        url = self.get_url(q=addressline, postcode=zip_code)
        try:
            response = requests.get(url)
        except:
            pass
        else:
            if response.ok:
                try:
                    self.response = response.json()
                except:
                    pass

    def get_url(self, **kwargs):
        return f'{self.api_url}?{urlencode(kwargs)}'


def upload_logo_to(instance, name):
    new_name = get_random_string(length=5)
    _, extension = name.split('.')
    if extension not in ['png', 'jpg', 'jpeg']:
        raise ValidationError('File extension should be png, jpg or jpeg')
    return f'business/{new_name}.{extension}'
