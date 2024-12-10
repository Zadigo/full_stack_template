from django.core.cache import cache
from django_seo.models import LegalBusiness, SearchEngineDetail


def load_from_cache(name, model):
    """Load the SEO from cache"""
    latest_item = cache.get(name, None)
    if latest_item is None:
        latest_item = model.objects.get_latest_version()
        if latest_item is None:
            return {name: {}}
        cache.set(name, latest_item, timeout=3600)
    return {name: latest_item}


def seo(request):
    """Load the SEO data into the templates"""
    return load_from_cache('seo', SearchEngineDetail)


def legal_business(request):
    """Load legal business infos to the templates"""
    return load_from_cache('legal_business', LegalBusiness)
