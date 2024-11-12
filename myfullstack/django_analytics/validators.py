import re
from django.core.exceptions import ValidationError

GOOGLE_ANALYTICS_REGEX = re.compile(r'^(?:G|AW|GTM)\-[A-Z0-9]{5,15}$')


def google_analytics_validator(value):
    result = GOOGLE_ANALYTICS_REGEX.match(value)
    if not result:
        raise ValidationError('Google Analytics tag is not valid. '
                              'Expects G/OPT/GTM-XXXXXXX.')
