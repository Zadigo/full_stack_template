import threading
from django.utils.encoding import smart_str


# DJANGO_MOBILE_STORAGE_BACKENDS = {

# }

_local_thread = threading.local()


# class DjangoMobileSessionBackend:
#     def get(self, request):
#         return getattr(request.session, 'django_mobile', {})

#     def set(self, request, state):
#         request.session['django_mobile'] = {
#             'is_mobile': state
#         }


# class DjangoMobileCookieBackend:
#     pass
#     # def get(self, request):
#     #     return request.COOKIES.get('django_mobile', {})

#     # def set(self, request, state):
#     #     request.COOKIES['django_mobile'] = state
#     #     setattr(request, '_django_mobile_cookie', state)

#     # def save(self, request, response):
#     #     if hasattr(request, '_django_mobile_cookie'):
#     #         response.set_cookie(
#     #             smart_str('django_mobile'),
#     #             smart_str(request._django_mobile_cookie),
#     #             httponly=True
#     #         )


# class DjangoMobileStorage:
#     pass


# django_mobile_storage = DjangoMobileStorage()


def set_mobile_state(state, request, persistent=False):
    """Sets the mobile state on the local thread
    and in the Django request"""
    request.is_mobile = state
    if persistent:
        request.session['is_mobile'] = state
    setattr(_local_thread, 'is_mobile', state)


def get_mobile_state(request):
    """Gets the current mobile state for the
    incoming request"""
    initial_result = getattr(request, 'is_mobile', getattr(_local_thread, 'is_mobile', False))
    return initial_result or getattr(request.session, 'is_mobile', False)
