from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


def base_error_response(request):
    return Response(status=status.HTTP_404_NOT_FOUND)


def base_bad_request_response(request, message: str):
    message = {'error': message}
    return Response(data=message, status=status.HTTP_400_BAD_REQUEST)


def not_authorized_response(request):
    return Response({'error': 'Not authorized'}, status=status.HTTP_401_UNAUTHORIZED)


def base_internal_server_error(request, message):
    return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['post'])
def subscribe_user(request):
    email = request.data.get('email')
    if email is None:
        return base_error_response(request)
    return Response({})


