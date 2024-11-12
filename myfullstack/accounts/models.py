import pathlib
from uuid import uuid4

from accounts.managers import CustomUserManager
from accounts.utils import upload_avatar_directory
from accounts.validators import (avatar_validator, stripe_card_validator,
                                 stripe_iban_validator, stripe_token_validator)
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from imagekit.models.fields import ProcessedImageField
from imagekit.processors import ResizeToCover


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        unique=True
    )
    email = models.EmailField(
        blank=False,
        null=False,
        unique=True
    )
    firstname = models.CharField(
        max_length=60,
        blank=True,
        null=True
    )
    lastname = models.CharField(
        max_length=60,
        blank=True,
        null=True
    )
    is_admin = models.BooleanField(
        default=False
    )
    is_staff = models.BooleanField(
        default=False
    )
    is_active = models.BooleanField(
        default=False
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f'{self.firstname} {self.lastname}'

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


class UserProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE
    )
    avatar = ProcessedImageField(
        upload_to=upload_avatar_directory,
        validators=[avatar_validator],
        processors=[ResizeToCover(100, 100)],
        format='JPEG',
        options={'quality': 80},
        blank=True
    )
    customer_id = models.CharField(
        max_length=100,
        validators=[stripe_token_validator],
        blank=True,
        null=True
    )
    payments = models.ManyToManyField(
        'Payment',
        blank=True
    )
    addresses = models.ManyToManyField(
        'Address',
        blank=True
    )
    created_on = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.email}'


class Payment(models.Model):
    reference = models.UUIDField(
        default=uuid4()
    )
    card = models.CharField(
        max_length=150,
        validators=[stripe_card_validator]
    )
    iban = models.CharField(
        max_length=150,
        validators=[stripe_iban_validator]
    )

    class Meta:
        verbose_name = _('payment')

    def __str__(self):
        return self.reference


class Address(models.Model):
    street_address = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    zip_code = models.CharField(
        max_length=10,
        blank=False,
        null=False
    )
    country = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return f'{self.street_address}'

    def get_full_address(self):
        return f'{self.street_address}, {self.zip_code}, {self.country}'


class Subscriber(models.Model):
    email = models.EmailField(unique=True, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_delete, sender=UserProfile)
def delete_avatar(instance, **kwargs):
    is_s3_backend = getattr(settings, 'USE_S3', False)
    if not is_s3_backend:
        try:
            path = pathlib.Path(instance.avatar.url.path)
        except:
            return
        else:
            if path.exists() and path.is_file():
                path.unlink()
    else:
        instance.url.delete()


@receiver(pre_save, sender=UserProfile)
def delete_avatar_on_update(instance, **kwargs):
    is_s3_backend = getattr(settings, 'USE_S3', False)
    if not is_s3_backend:
        if instance.pk:
            try:
                old_avatar = UserProfile.objects.get(pk=instance.pk)
            except:
                return
            else:
                if old_avatar and old_avatar != instance.avatar.url:
                    path = pathlib.Path(instance.avatar.url.path)
                    if path.exists() and path.is_file():
                        path.unlink()
    else:
        instance.avatar.url.delete()
