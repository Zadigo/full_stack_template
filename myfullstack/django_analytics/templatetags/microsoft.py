from django.template import Library
from django_analytics.utils import load_from_cache

register = Library()


@register.inclusion_tag('microsoft/clarity.html')
def clarity():
    result = load_from_cache(key='clarity')
    return {'clarity_id': result}
