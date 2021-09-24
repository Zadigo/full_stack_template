from accounts import get_userprofile_model
from accounts.models import Address, MyUserProfile
from api import check_user_token, serializers
from api.serializers.profile import (AddressSerializer,
                                     MyUserProfileSerializer,
                                     PasswordChangeValidationSerializer,
                                     PersonalDetailsValidationSerializer)
from api.views import mixins
from api.views.base import (base_bad_request_response, base_error_response,
                            base_internal_server_error,
                            not_authorized_response)
from api.views.mixins import CustomIsAuthenticated
from django.contrib.auth import (get_user_model, password_validation,
                                 update_session_auth_hash)
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin, RetrieveModelMixin,
                                   UpdateModelMixin)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from accounts.models import MyUserProfile

USER_MODEL = get_user_model()


# class ChangePersonalDetails(GenericAPIView):
#     http_method_names = ['post', 'patch']
#     # Dynamically update the data depending 
#     # on the incoming position that was
#     # included in the incoming POST data
#     serializer_classes = [
#         PersonalDetailsValidationSerializer
#     ]

#     def post(self, request, **kwargs):
#         position = request.data.get('position', None)
#         if position is not None:
#             position = int(position)
#         else:
#             return Response({'error': 'An error occured - PF1'})
            
#         content = request.data['content']
#         if not content or content is None:
#             return Response(data={'state': True}, status=status.HTTP_202_ACCEPTED)

#         serializer = self.get_serializer(position, content)
#         serializer.update(request.user, serializer._validated_data)
#         return Response(data=serializer.data)

#     def get_serializer(self, position, data):
#         serializer = self.serializer_classes[position]
#         instance = serializer(data=data)
#         instance.is_valid(raise_exception=True)
#         return instance


# class ChangePassword(mixins.GlobalAPIMixins, GenericAPIView):
#     queryset = USER_MODEL.objects.all()
#     serializer_class = serializers.UserSerializer

#     def post(self, request, **kwargs):
#         old_password = request.data['old_password']
#         user = authenticate(
#             request,
#             username=request.user.username,
#             password=old_password
#         )
#         if user is None:
#             return Response({'error': 'User does not exist'})

#         password1 = request.data['password1']
#         password2 = request.data['password2']

#         if password1 != password2:
#             pass

#         if password1 == old_password:
#             pass

#         user.set_password(password1)
#         user.save()
#         update_session_auth_hash(request, user)
#         return Response({'state': True})


class AddressesApi(GenericViewSet, ListModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [CustomIsAuthenticated]

    def get_queryset(self, request):
        queryset = super().get_queryset()
        return queryset.filter(myuserprofile__id=request.user.id)

    def get_object(self):
        # Overrides the default get_object() to ensure that
        # a person viewing an address is well his own
        queryset = self.filter_queryset(self.get_queryset())
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        if lookup_url_kwarg not in self.kwargs:
            return Response(status=status.HTTP_404_NOT_FOUND)

        filter_kwargs = {
            self.lookup_field: int(self.kwargs[lookup_url_kwarg]),
            'myuserprofile__id': self.request.user.id
        }
        address = get_object_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, address)
        return address

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset(request)
        serializer = self.get_serializer(queryset, many=True)
        return Response(data=serializer.data)

    def perform_create(self, serializer, request):
        new_address = serializer.save()
        user_profile = get_object_or_404(MyUserProfile, id=request.user.id)
        user_profile.addresses.add(new_address)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, request)
        headers = self.get_success_headers(serializer.data)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED, headers=headers)


@api_view(['post', 'patch'])
def update_personal_details(request):
    if not check_user_token(request):
        return not_authorized_response(request)

    serializer_classes = [
        PersonalDetailsValidationSerializer
    ]

    def _get_serializer(position, data):
        serializer_class = serializer_classes[position]
        serializer_instance = serializer_class(data=data)
        serializer_instance.is_valid(raise_exception=True)
        return serializer_instance

    serializer_position = request.data.get('position', None)
    if serializer_position is not None:
        serializer_position = int(serializer_position)
    else:
        return base_internal_server_error(request, 'An error occured - PF1')

    details = request.data.get('details')
    if not details or details is None:
        return Response({}, status=status.HTTP_202_ACCEPTED)

    serializer = _get_serializer(serializer_position, details)
    serializer.update(request.user, serializer.validated_data)
    return Response(data=serializer.data)


@api_view(['post'])
def update_preferences(request):
    if not check_user_token(request):
        return not_authorized_response(request)
    return Response({'status': 'Great'})


@api_view(['get'])
def collect_user_details(request):
    if not check_user_token(request):
        return not_authorized_response(request)
    
    user_profile = get_object_or_404(MyUserProfile.objects.all(), id=request.user.id)
    serializer = MyUserProfileSerializer(instance=user_profile)
    return Response(serializer.data)


@api_view(['post'])
def change_password(request, **kwargs):
    if not check_user_token(request):
        return base_error_response(request)

    serializer = PasswordChangeValidationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    old_password = request.data.get('old_password')

    user = get_object_or_404(USER_MODEL.objects.all(), id=request.user.id)
    password_validation.validate_password(
        old_password, request.user, password_validators=[])

    result, message = serializer.update(request, instance=user)
    if not result:
        return base_bad_request_response(request, message)
    update_session_auth_hash(request, user)
    return Response({'message': 'Password changed'})
