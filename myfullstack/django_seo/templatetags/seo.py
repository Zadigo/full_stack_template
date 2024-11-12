import json
from urllib.parse import urlparse

from django.conf import settings
from django.core.cache import cache
from django.template import Library, Node
from django.template.exceptions import TemplateSyntaxError

register = Library()


# class WebsiteSEONode(Node):
#     def __init__(self, extra_context, keys, key=None):
#         self.key = key
#         self.keys = keys
#         self.extra_context = extra_context or {}

#     def render(self, context):

#         return ''


# @register.simple_tag(takes_context=True)
# def website_seo(context, key=None):
#     """Implement SEO functionnalities
#     in the website"""
#     items = ['SEO_SOCIALS']

#     def get_setting(name):
#         return name, getattr(settings, name, {})

#     result = list(map(get_setting, items))

#     keys = ', '.join(x[0] for x in result)

#     extra_context = {}
#     for name, value in result:
#         _, rhv = name.split('_', 1)
#         extra_context.update({rhv.lower(): value})
#     context.push(seo=extra_context)

#     if key is not None:
#         try:
#             context.push(**{key: extra_context[key]})
#         except KeyError:
#             raise TemplateSyntaxError(
#                 f'Could not find {key} in items. Valid keys are: {keys}')
#     return ''


@register.filter(name='canonical')
def canonical(url):
    """In order to prevent urls with a query from
    being explicity indexed by Google, this function
    will partition the url in order to return only
    the host and the path.

    In order words, `http://example.com` and `http://example.com?q=1`
    will resolve to `http://example.com` being
    the single source."""
    url_object = urlparse(url)
    if url_object.query:
        new_url = f'{url_object.scheme}://{url_object.netloc}{url_object.path}'
        return new_url
    return url


@register.inclusion_tag('page_title.html', takes_context=True)
def page_title(context, title):
    from django_seo.models import LegalBusiness

    business = cache.get('legal_business', None)
    if business is None:
        business = LegalBusiness.objects.get_latest_version()
        cache.set('business', business, timeout=6400)
    context.push({'title': title, 'legal_business': business})
    return context


@register.simple_tag(name='country')
def country(name, sub_key=None):
    """Returns a specific country from a
    list of countries. If the sub key is
    specified, will return only the specific
    country element from the countries data"""
    data = cache.get('countries')

    base_path = getattr(settings, 'BASE_DIR')
    filepath = base_path.joinpath('django_seo', 'media', 'countries.json')

    if data is None:
        with open(filepath, mode='r', encoding='utf-8') as f:
            data = json.load(f)
            cache.set('countries', data)

    item = list(filter(lambda x: x['name'] == name, data))[-1]
    if sub_key is not None:
        return item[sub_key]
    return item
