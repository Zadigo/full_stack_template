from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_account_creation_email():
    pass
