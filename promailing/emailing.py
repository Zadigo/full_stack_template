import random
from logging import warning
from urllib.parse import urljoin
from django.core.exceptions import ImproperlyConfigured
from django.apps import apps
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.template import loader

from promailing.shortcuts import generate_code

DEFAULT_EMAIL_VERIFICATION_BACKEND = 'promailing.EmailVerificationCode'


class BackendMixin:
    """Backend for classes that require using
    a model for storing data"""

    def __init__(self, user):
        self._user = user

    def use_backend(self):
        try:
            path = getattr(settings, 'EMAIL_VERIFICATION_BACKEND',
                           DEFAULT_EMAIL_VERIFICATION_BACKEND)
            backend = apps.get_model(path)
        except:
            raise ImproperlyConfigured(
                "There is no verification code model backend")
        else:
            verification_code = generate_code()
            return backend.objects.create(user=self._user, verification_code=verification_code)


class ConfirmationEmails:
    """Main class for all email senders"""
    subject_template_name = None
    email_template_name = None

    @property
    def get_host_user(self):
        try:
            return settings.EMAIL_HOST_USER
        except:
            raise ValueError('You should set an EMAIL_HOST_USER')

    def get_context(self, **kwargs):
        return {**kwargs}

    def clean(self, context):
        return context

    def client(self, context, from_email, to_email, html_template_name=None):
        if not self.email_template_name:
            raise ValueError(
                "Cannot send email without specifiying 'email_template_name'")

        subject = loader.render_to_string(self.subject_template_name, context)
        subject = ''.join(subject.splitlines())

        body = loader.render_to_string(self.email_template_name, context)
        email = EmailMultiAlternatives(
            subject, body, from_email=from_email, to=[to_email])

        if html_template_name is not None:
            html_email = loader.render_to_string(html_template_name, context)
            email.attach(html_email, 'text/html')

        email.send()

    def send_email(self, to_email, context={}, request=None, **kwargs):
        """Entrypoint for sending an email"""
        context = self.get_context(**context)
        self.client(context, self.get_host_user, to_email)


class VerifyAccount(BackendMixin, ConfirmationEmails):
    subject_template_name = 'verify_account/subject.txt'
    email_template_name = 'verify_account/text_page.txt'

    def get_context(self, **kwargs):
        context = super().get_context(**kwargs)
        context['username'] = self._user.get_full_name()
        context['website_name'] = 'Google'
        context['verification_link'] = 'http://localhost:3000?redirect=verify'
        return context

    def send_email(self, **kwargs):
        # Only allow email verification for
        # non active users
        if not self._user.is_active:
            to_email = self._user.email
            instance = self.use_backend()

            # Fail silently if we cannot send an email
            if instance is not None:
                context = self.get_context()
                context['verification_code'] = instance.verification_code
                super().send_email(to_email, context=context, **kwargs)


class ResetPassword(BackendMixin, ConfirmationEmails):
    subject_template_name = 'password_reset/subject.txt'
    email_template_name = 'password_reset/text.txt'

    def send_email(self, **context):
        if not self._user.is_active:
            to_email = self._user.email
            instance = self.use_backend()

            # Fail silently if we cannot send an email
            if instance is not None:
                context = self.get_context()
                context['verification_code'] = instance.verification_code
                super().send_email(to_email, context=context)


# @staticmethod
#  def _check_kwargs(values):
#     required = [
#         'estimated_order_date',
#         'customer_delivery_address',
#         'order_reference',
#         'order_quantity',
#         'order_total',
#         'customer_name'
#         ]
#     for item in required:
#         keys = values.keys()
#         if item not in keys:
#             values.update({item: 'NOT_SET'})
#     return values

# class OrderConfirmationEmail(ConfirmationEmails):
#     email_template_name = 'components/emails/confirmation_email.html'


# class ExpeditionEmail(ConfirmationEmails):
#     email_template_name = 'components/emails/expedition_email.html'


# class FailedOrderEmail(ConfirmationEmails):
#     email_template_name = 'components/emails/failed_email.html'

#     def process(self, request, order_reference, transaction, customer_name):
#         context = {
#             'order_reference': order_reference,
#             'transaction': transaction,
#             'customer_name': customer_name
#         }
#         email_host_user = self._get_email_host_user()
#         self.send_email(context, email_host_user, email_host_user)
