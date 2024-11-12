# Promailing

## Presentation

Send professional enterprise emails with Django to your users

## How to use

```python
PROMAILING_EMAIL_VERIFICATION_BACKEND = 'accounts.EmailVerificationCode'

PROMAILING_EMAIL_VERIFICATION_LINK = 'http://localhost:3000?redirect=verify'
```

### Email verification

#### PROMAILING_EMAIL_VERIFICATION_BACKEND

Promailing uses the default `EmailVerificationCode` model to validations. You can swap this model with your own custom model using this setting.

#### PROMAILING_EMAIL_VERIFICATION_REDIRECT

Once the verification is complete, Promailing will need to indicate to the user the page he needs to access in order to verify his account. Use this setting to customize this. Defaults `http://.../verify-account`.

#### How to use

```python
from promailing.emailing import VerifyAccount

user = User.objects.first()
instance = VerifyAccount(user)
instance.send_email(context={})
```

