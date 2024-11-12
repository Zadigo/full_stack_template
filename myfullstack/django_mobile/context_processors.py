from django_mobile import get_mobile_state


def is_mobile(request):
    """Context processor indicating in a template
    if a request comes from a mobile phone"""
    return {'is_mobile': get_mobile_state(request)}
