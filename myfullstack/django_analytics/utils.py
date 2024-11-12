import logging

from django.core.cache import cache


def load_from_cache(key=None):
    """Loads the latest analytics configuration
    from the cache in order to improve performance"""
    from django_analytics.models import AnalyticsVersion

    latest_version = cache.get('analytics_latest_version', None)
    if latest_version is None:
        latest_version = AnalyticsVersion.objects.get_latest_version()
        cache.set('analytics_latest_version', latest_version, timeout=3600)
    
    value = getattr(latest_version, key, None)
    if value is None:
        logging.warning(f'Analytics tag "{key}" is empty')
        return ''
    return value


def load_default(key=None, tag=None):
    """Loads the default user provided tag or
    the one stored in the database

    >>> # Will return a tag from the database
    ... # if it exists
    ... {% google_analytics %}
    >>> # Will return the user provided value
    ... {% google_analytics tag="G-XXXX" %}
    """
    return tag or load_from_cache(key=key)
