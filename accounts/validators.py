from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_image_file_extension


def email_validator(value):
    errors = []
    incoming_domain = value.split('@')[-1]
    acceptable_domains = ['google', 'outlook']
    for domain in acceptable_domains:
        if domain not in incoming_domain:
            errors.append(domain)
            continue
        else:
            errors = []
            break
    if errors:
        raise ValidationError('Domain is not valid')


def stripe_token_validator(value):
    pass


def stripe_card_validator(value):
    pass


def stripe_iban_validator(value):
    pass


def password_validator(value):
    def default_length(value):
        if len(value) < 20:
            raise ValidationError('Password should be above 30 in length')
    validate_password(value, password_validators=[default_length])


def username_validator(value):
    pass


def avatar_validator(instance):
    result = validate_image_file_extension(instance)(
        allowed_extensions=['jpg', 'jpeg', 'png'])
    if not result:
        raise ValidationError('Image is not valid')
    if instance.size > 10000:
        raise ValidationError('Image exceeds acceptable file size')
