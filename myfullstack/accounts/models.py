
import pathlib
from uuid import uuid4

from accounts.managers import CustomUserManager
from accounts.validators import stripe_card_validator, stripe_iban_validator
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        verbose_name=_('username'),
        max_length=150,
        unique=True,
        blank=True,
        null=True,
        validators=[username_validator]
    )
    email = models.EmailField(
        verbose_name=_('email address'),
        unique=True
    )
    firstname = models.CharField(
        verbose_name=_('firstname'),
        max_length=150,
        blank=True
    )
    lastname = models.CharField(
        verbose_name=_('lastname'),
        max_length=150,
        blank=True
    )
    is_staff = models.BooleanField(
        verbose_name=_("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can "
            "log into this admin site."
        ),
    )
    is_active = models.BooleanField(
        verbose_name=_("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    created_on = models.DateTimeField(
        verbose_name=_('date joined'),
        default=timezone.now
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('custom user')
        verbose_name_plural = _('custom users')
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.get_full_name()}'

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        return f'{self.firstname} {self.lastname}'

    def get_short_name(self):
        return self.firstname

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


class UserProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        models.CASCADE,
        related_name='user_profile'
    )
    avatar = models.ImageField(
        blank=True,
        null=True
    )
    avatar_thumbnail = ImageSpecField(
        source='avatar',
        processors=[ResizeToFill(100, 100)],
        format='JPEG',
        options={'quality': 80}
    )
    created_on = models.DateTimeField(
        verbose_name=_('date joined'),
        default=timezone.now
    )

    def __str__(self):
        return f'Profile for {self.user.email}'


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
            old_avatar = UserProfile.objects.get(pk=instance.pk)
            if old_avatar and old_avatar != instance.avatar:
                path = pathlib.Path(instance.avatar.url.path)
                if path.exists() and path.is_file():
                    path.unlink()
    else:
        instance.avatar.url.delete()
