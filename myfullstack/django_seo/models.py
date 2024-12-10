import pathlib

from django.conf import settings
from django.db import models
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch.dispatcher import receiver
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _
from django_seo import validators
from django_seo.choices import CompanyTypes
from django_seo.managers import GlobalManager
from django_seo.utils import upload_logo_to
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


class BaseAbstract(models.Model):
    version = models.PositiveIntegerField(default=0)
    modified_on = models.DateField(auto_now_add=True)
    created_on = models.DateField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['version']

    def full_name(self):
        return f'Version {self.version}'


class PageDetail(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )
    social_title = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    social_image = ProcessedImageField(
        processors=ResizeToFill(width=1200, height=630),
        blank=True,
        null=True,
        format='JPEG',
        options={
            'quality': 100
        }
    )
    social_description = models.TextField(
        max_length=155,
        blank=True,
        null=True
    )
    keywords = models.CharField(
        max_length=100,
        help_text='Meta keywords',
        blank=True,
        null=True
    )
    description = models.TextField(
        max_length=155,
        help_text=_(
            "Description which should ideally be "
            "between a 100 and 155 characters which is "
            "specific to a given page"
        ),
        blank=True,
        null=True
    )
    same_descriptions = models.BooleanField(
        default=True
    )
    created_on = models.DateField(
        auto_now=True
    )

    def __str__(self):
        return f'{self.pk}'


class SearchEngineDetail(BaseAbstract):
    """Stores all the SEO elements for
    the current website"""

    author = models.CharField(
        max_length=100,
        help_text=_(
            "Author or founder of "
            "the company'"
        ),
        blank=True,
        null=True
    )
    company_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    keywords = models.CharField(
        max_length=100,
        help_text='Meta keywords',
        blank=True,
        null=True
    )
    description = models.TextField(
        max_length=155,
        help_text=_(
            "Description which should ideally be "
            "between a 100 and 155 characters. This is "
            "a global description for a all the pages"
        ),
        blank=True,
        null=True
    )
    pages = models.ManyToManyField(
        PageDetail,
        blank=True
    )
    theme_color = models.CharField(
        max_length=20,
        default='2d2d2d',
        blank=True,
        null=True
    )
    linkedin = models.URLField(
        help_text=_('LinkedIn business page'),
        blank=True,
        null=True
    )
    facebook = models.URLField(
        help_text=_('Facebook business page'),
        blank=True,
        null=True
    )
    instagram = models.URLField(
        help_text=_('Instagram profile page'),
        blank=True,
        null=True
    )
    twitter = models.URLField(
        help_text=_('Twitter business page'),
        blank=True,
        null=True
    )
    youtube = models.URLField(
        help_text=_('YouTube channel'),
        blank=True,
        null=True
    )
    tiktok = models.URLField(
        help_text=_('Tiktok page'),
        blank=True,
        null=True
    )

    objects = GlobalManager.as_manager()

    def __str__(self):
        return f'SEO Version: {self.version}'

    @cached_property
    def get_socials(self):
        return {
            'facebook': self.facebook,
            'twitter': self.twitter,
            'instagram': self.instagram,
            'linkedin': self.linkedin,
            'youtube': self.youtube,
            'tiktok': self.tiktok
        }


class LegalBusiness(BaseAbstract):
    """Regroups legal information about the
    current business"""

    legal_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    registration_place = models.CharField(
        max_length=200,
        help_text=_("Place where the company was registered"),
        blank=True,
        null=True
    )
    company_type = models.CharField(
        max_length=2,
        help_text=_("'A' for commerce, 'B' for company"),
        choices=CompanyTypes.choices,
        default=CompanyTypes.B
    )
    siren = models.CharField(
        max_length=9,
        validators=[validators.validate_siren],
        verbose_name='SIREN',
        unique=True,
        blank=True,
        null=True
    )
    siret = models.CharField(
        max_length=14,
        validators=[validators.validate_siret],
        verbose_name='SIRET',
        unique=True,
        blank=True,
        null=True
    )
    ape = models.CharField(
        max_length=5,
        blank=True,
        null=True,
        verbose_name='Code APE',
        help_text=_("The APE code for the business"),
        validators=[validators.validate_ape]
    )
    founding_date = models.DateField(
        blank=True,
        null=True
    )
    general_email = models.EmailField(
        validators=[],
        blank=True,
        null=True
    )
    customer_service_email = models.EmailField(
        validators=[],
        blank=True,
        null=True
    )
    telephone = models.CharField(
        max_length=100,
        validators=[],
        blank=True,
        null=True
    )
    address_line = models.CharField(
        max_length=300,
        blank=True,
        null=True
    )
    locality = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    region = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    postal_code = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    country = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    logo = models.ImageField(
        upload_to=upload_logo_to,
        help_text=_("Ideally should be a square e.g. 200x200"),
        blank=True,
        null=True
    )
    square_image = ImageSpecField(
        source='logo',
        processors=[ResizeToFill(100, 100)],
        options={'quality': 100},
        format='PNG'
    )

    objects = GlobalManager.as_manager()

    class Meta:
        verbose_name_plural = _('legal businesses')
        ordering = ['version']

    def __str__(self):
        return f'Business Version: {self.version}'

    @cached_property
    def get_socials(self):
        return {
            'facebook': self.facebook,
            'twitter': self.twitter,
            'instagram': self.instagram,
            'linkedin': self.linkedin,
            'youtube': self.youtube,
            'tiktok': self.tiktok
        }

    @cached_property
    def address(self):
        """The full company's address"""
        return f'{self.address_line}, {self.postal_code}, {self.region}'

    @cached_property
    def rcs_number(self):
        """This represents the RCS number that is used to
        register a company in France"""
        registration_place = None
        if self.registration_place is not None:
            self.registration_place = registration_place
        return f'RCS {registration_place} {self.company_type} {self.siren}'


@receiver(post_save, sender=SearchEngineDetail)
def update_version(instance, created, **kwargs):
    if created:
        result = SearchEngineDetail.objects.latest('created_on')
        instance.version = result.version + 1
        instance.save()


@receiver(pre_save, sender=LegalBusiness)
def validate_address(instance, **kwargs):
    pass


@receiver(pre_save, sender=LegalBusiness)
def update_logo(instance, **kwargs):
    is_s3_backend = getattr(settings, 'USE_S3', False)
    if is_s3_backend:
        instance.logo.delete(save=False)
    else:
        if instance.pk:
            try:
                business = LegalBusiness.objects.get_latest_version()
            except:
                return False

            new_logo = instance.logo
            if business and business.logo != new_logo:
                try:
                    path = pathlib.Path(new_logo.path)
                except:
                    return False
                else:
                    if path.is_file() and path.exists():
                        path.unlink()


@receiver(post_delete, sender=LegalBusiness)
def delete_logo(instance, **kwargs):
    is_s3_backend = getattr(settings, 'USE_S3', False)
    if is_s3_backend:
        instance.logo.delete(save=False)
    else:
        if instance.logo:
            try:
                path = pathlib.Path(instance.logo.path)
            except:
                return False
            else:
                if path.is_file() and path.exists():
                    path.unlink()


@receiver(post_save, sender=PageDetail)
def update_descriptions(instance, created, **kwargs):
    if created:
        if instance.same_descriptions:
            if instance.description:
                instance.social_description = instance.description
                instance.save()
