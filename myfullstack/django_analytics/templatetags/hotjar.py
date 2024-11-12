from django.template import Library

from django_analytics.utils import load_default

register = Library()


@register.inclusion_tag('hotjar.html')
def hotjar(site_id=None):
    """Implements Hotjar"""
    site_id = load_default(key='hotjar', tag=site_id)
    return {'site_id': site_id}
