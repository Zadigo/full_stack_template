import json
from urllib.parse import urlparse

from django.conf import settings
from django.core.cache import cache
from django.template import Library
from django_seo.models import SearchEngineDetail
from django.template.context import Context
from django.core.exceptions import ObjectDoesNotExist

register = Library()


@register.filter(name='canonical')
def canonical(url):
    """In order to prevent urls with a query from
    being explicity indexed by Google, this function
    will partition the url in order to return only
    the host and the path.

    In order words, `http://example.com` and `http://example.com?q=1`
    will resolve to `http://example.com` being
    the single source"""
    url_object = urlparse(url)
    if url_object.query:
        new_url = f'{url_object.scheme}://{url_object.netloc}{url_object.path}'
        return new_url
    return url


@register.inclusion_tag('page_title.html', takes_context=True)
def page_title(context, title):
    """Customizes the page title by adding the branding
    or the company name"""
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


@register.inclusion_tag('social_metatags.html', takes_context=True)
def social_metatags(context, page_name):
    page_titles = cache.get('page_titles', None)
    if page_titles is None:
        seo = SearchEngineDetail.objects.get_latest_version()
        if seo:
            page_titles = seo.pages.all()
            cache.set('page_titles', page_titles, timeout=(1 * 60))

    if not page_titles:
        return None

    try:
        page = page_titles.get(name=page_name)
    except ObjectDoesNotExist:
        raise ObjectDoesNotExist(
            f"Page with name {page_name} does not "
            "exist on the database"
        )
    else:
        context.push({'page_seo': page})
        return context
