from uuid import uuid4

from django.contrib.auth.models import AbstractBaseUser, Group, Permission
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from imagekit.models.fields import ProcessedImageField
from imagekit.processors import ResizeToCover
from rest_framework.authtoken.models import Token

from accounts.managers import MyUserManager
from accounts.utils import upload_avatar_directory
from accounts.validators import (stripe_card_validator, stripe_iban_validator,
                                 stripe_token_validator)


class PermissionMixin(models.Model):
    is_superuser = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, blank=True, related_name='user_set', related_query_name='user')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='user_set', related_query_name='user')

    class Meta:
        abstract = True

    def has_perm(self, perm, obj=None):
        if self.is_active and (self.is_superuser or self.is_admin):
            return True
        return False

    def has_module_perms(self, app_label):
        if self.is_active and (self.is_superuser and self.is_admin):
            return True
        return False


class MyUser(AbstractBaseUser, PermissionMixin):
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(blank=False, null=False, unique=True)
    
    firstname = models.CharField(max_length=60, blank=True, null=True)
    lastname = models.CharField(max_length=60, blank=True, null=True)
    
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    created_on = models.DateTimeField(auto_now_add=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f'{self.firstname} {self.lastname}'

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


class MyUserProfile(models.Model):
    myuser = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    avatar = ProcessedImageField(
        upload_to=upload_avatar_directory,
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

    payments = models.ManyToManyField('Payment', blank=True)
    addresses = models.ManyToManyField('Address', blank=True)

    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.myuser.email


class Payment(models.Model):
    reference = models.UUIDField(default=uuid4())
    card = models.CharField(max_length=150, validators=[stripe_card_validator])
    iban = models.CharField(max_length=150, validators=[stripe_iban_validator])

    def __str__(self):
        return self.reference


class Address(models.Model):
    street_address = models.CharField(max_length=100, blank=False, null=False)
    zip_code = models.CharField(max_length=10, blank=False, null=False)
    country = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return self.street_address

    def get_full_address(self):
        return f'{self.street_address}, {self.zip_code}, {self.country}'


class Subscriber(models.Model):
    email = models.EmailField(unique=True, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


@receiver(post_save, sender=MyUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = MyUserProfile.objects.create(myuser=instance)
        
        # Automatically create a Stripe
        # customer and save it to the
        # profile
        user_profile.customer_id = 'some_id'
        user_profile.save()


        # Finally, create the authentication
        # token that will be used by the user
        # via the api
        Token.objects.create(user=user_profile.myuser)
