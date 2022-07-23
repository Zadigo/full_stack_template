import random

from django.http import Http404, HttpResponseForbidden
from django.shortcuts import _get_queryset


def generate_code():
    items = [f"{random.randrange(0, 9)}" for _ in range(4)]
    return int(''.join(items))


def verify_user_code(*args, **kwargs):
    from promailing.models import EmailVerificationCode
    queryset = _get_queryset(EmailVerificationCode)
    try:
        instance = queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        raise Http404('Verification code is not valid')
    else:
        if instance.expired:
            raise HttpResponseForbidden('Code is not valid')
        return instance
