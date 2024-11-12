from django.template import Library

from django_analytics.utils import load_default

register = Library()


@register.inclusion_tag('facebook/pixel.html')
def facebook(pixel_id=None):
    """Implements Hotjar"""
    pixel_id = load_default(key='facebook_pixel', tag=pixel_id)
    return {'pixel_id': pixel_id}
