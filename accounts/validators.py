from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_image_file_extension
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError as RestValidationError


def email_validator(value):
    pass
    # is_valid = False
    # incoming_domain = value.split('@')[-1]
    # acceptable_domains = ['gmail', 'outlook']
    # for domain in acceptable_domains:
    #     if domain in incoming_domain:
    #         is_valid = True
    #         break

    # if not is_valid:
    #     raise RestValidationError(
    #         _("Domain in email is not valid. Should be one of %(domains)s") % {
    #             'domains': ', '.join(acceptable_domains)
    #     })


def stripe_token_validator(value):
    pass


def stripe_card_validator(value):
    pass


def stripe_iban_validator(value):
    pass


def password_validator(value):
    class CheckLength:
        @staticmethod
        def validate(password, user=None):
            print(password, user)
            if len(password) < 20:
                raise RestValidationError(
                    detail=_('Password should be above 30 in length'))
    validate_password(value, password_validators=[CheckLength])


def username_validator(value):
    invalid_characters = ['@', '-', '#', ',', ';',
                          ':', '!', '*', '$', '£', '+', '=', '~']
    errors = list(filter(lambda x: x in invalid_characters, value))
    # for x in value:
    #     if x in invalid_characters:
    #         errors.append(x)
    if errors:
        raise RestValidationError(
            detail=_("Invalid characters in username: %(characters)s") % {
                'characters': ', '.join(errors)
            }
        )


def avatar_validator(instance):
    result = validate_image_file_extension(instance)(
        allowed_extensions=['jpg', 'jpeg', 'png'])

    if not result:
        raise ValidationError(_('Image is not valid'))

    if instance.size > 10000:
        raise ValidationError(_('Image exceeds acceptable file size'))
