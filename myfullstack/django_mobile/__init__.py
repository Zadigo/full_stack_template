import threading

_local_thread = threading.local()


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
    initial_result = getattr(request, 'is_mobile', getattr(
        _local_thread, 'is_mobile', False))
    return initial_result or getattr(request.session, 'is_mobile', False)
