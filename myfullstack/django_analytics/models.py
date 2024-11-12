from django.db import models
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from django.utils.translation import gettext_lazy as _

from django_analytics.managers import GlobalManager
from django_analytics.validators import google_analytics_validator


class BaseAbstract(models.Model):
    version = models.PositiveIntegerField(default=0)
    modified_on = models.DateField(auto_now_add=True)
    created_on = models.DateField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['version']

    def full_name(self):
        return f'Version {self.version}'


class AnalyticsVersion(BaseAbstract):
    """Stores related configuration
    parameters for analytics websites"""

    clarity = models.CharField(
        max_length=20,
        help_text=_('Microsoft clarity'),
        blank=True,
        null=True
    )
    google_analytics = models.CharField(
        max_length=15,
        help_text=_('Google Analytics tag'),
        validators=[google_analytics_validator],
        blank=True,
        null=True
    )
    google_ads = models.CharField(
        max_length=20,
        help_text=_('Google ads conversion ID'),
        validators=[google_analytics_validator],
        blank=True,
        null=True
    )
    google_tag_manager = models.CharField(
        max_length=15,
        help_text=_('Google Tag Manager container tag'),
        validators=[],
        blank=True,
        null=True
    )
    hotjar = models.CharField(
        max_length=50,
        help_text=_('Hotjar configuration tag'),
        blank=True,
        null=True
    )
    facebook_pixel = models.CharField(
        max_length=100,
        help_text=_('Facebook pixel ID'),
        blank=True,
        null=True
    )

    objects = GlobalManager.as_manager()

    def __str__(self):
        return f'Analytics Version: {self.version}'


@receiver(post_save, sender=AnalyticsVersion)
def update_version(instance, created, **kwargs):
    # Increment the version of the container
    # when the user implements additionnal
    # configurations
    if created:
        result = AnalyticsVersion.objects.latest('created_on')
        instance.version = result.version + 1
        instance.save()
