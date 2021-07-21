from rest_framework.response import Response
from rest_framework import status


def base_error_response(request):
    return Response(status=status.HTTP_404_NOT_FOUND)
