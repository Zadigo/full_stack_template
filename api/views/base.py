from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


def base_error_response(request):
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['post'])
def subscribe_user(request):
    email = request.data.get('email')
    if email is None:
        return base_error_response(request)
    return Response({})
