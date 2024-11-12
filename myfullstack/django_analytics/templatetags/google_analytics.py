from django.template import Library

from django_analytics.utils import load_default

register = Library()


@register.inclusion_tag('google/analytics.html')
def google_analytics(tag=None, currency='eur', debug=True):
    """Implements Google Analytics standalone tag"""
    tag = load_default(key='google_analytics', tag=tag)
    return {
        'analytics_tag': tag,
        'currency': currency,
        'debug': debug
    }


@register.inclusion_tag('google/ads/analytics.html', takes_context=True)
def analytics_and_ads(context, analytics_id=None, ads_id=None, debug=True):
    """Special tag to implement both Google Analytics
    and Google Ads in a Django project"""
    analytics_id = load_default(key='google_analytics', tag=analytics_id)
    ads_id = load_default(key='google_ads', tag=ads_id)
    data = {
        'analytics_tag': analytics_id,
        'google_ads_id': ads_id,
        'currency': 'eur',
        'debug': debug
    }
    context.push(data)
    return context


@register.inclusion_tag('google/tag_manager.html')
def google_tag_manager(tag=None):
    """Implements Google Tag Manager"""
    tag = load_default(key='google_tag_manager', tag=tag)
    return {'gtm_tag': tag}


@register.inclusion_tag('google/no_script.html')
def gtm_no_script(tag=None):
    """Implements anti-flicker script"""
    tag = load_default(key='google_tag_manager', tag=tag)
    return {'gtm_tag': tag}
