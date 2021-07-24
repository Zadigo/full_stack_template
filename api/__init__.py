from rest_framework import status


def check_user_token(request):
    from rest_framework.authtoken.models import Token

    token = request.META.get('HTTP_AUTHORIZATION', None)
    if token is None:
        return False
    _, token = token.split(' ', maxsplit=1)

    queryset = Token.objects.filter(key=token)
    if queryset.exists():
        try:
            true_value = queryset.get()
        except:
            true_value = None
        return request.user.is_authenticated and true_value is not None
    return False
