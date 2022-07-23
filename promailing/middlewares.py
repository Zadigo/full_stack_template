from django.contrib.auth.middleware import AuthenticationMiddleware


class FailedLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path_info = request.META.get('PATH_INFO')
        response = self.get_response(request)
        if path_info == '/api/v1/accounts/login':
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', None)
            if x_forwarded_for is not None:
                ip_address = x_forwarded_for.split(',')[0]
            else:
                ip_address = request.META.get('REMOTE_ADDR')
            print(ip_address)
        return response
