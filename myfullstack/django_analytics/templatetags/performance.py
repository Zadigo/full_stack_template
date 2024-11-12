from django.template import Library

register = Library()


@register.inclusion_tag('page_speed.html')
def page_performance():
    """Measures the speed performance of the current page"""
    return {}


@register.inclusion_tag('page_exceptions.html')
def page_exceptions():
    """Measures page exceptions"""
    return {}
