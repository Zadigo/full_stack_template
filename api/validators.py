from django.core.validators import RegexValidator, MinLengthValidator

def password_validator(password: str):
    length_validator = MinLengthValidator(limit_value=5)
    length_validator(password)
    return password
