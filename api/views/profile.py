from django import http
from accounts.models import Address, MyUserProfile
from accounts import get_userprofile_model
from api import serializers
from api.views import mixins
from django.contrib.auth import (authenticate, get_user_model,
                                 update_session_auth_hash)
from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.db.transaction import atomic
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from api import check_user_token
from api.views.mixins import CustomIsAuthenticated

USER_MODEL = get_user_model()

USER_PROFILE_MODEL = get_userprofile_model()


class ProfileDetails(GenericViewSet, RetrieveModelMixin):
    queryset = USER_PROFILE_MODEL.objects.all()
    serializer_class = serializers.MyUserProfileSerializer
    permission_classes = [IsAuthenticated]


class ChangePassword(mixins.GlobalAPIMixins, GenericAPIView):
    queryset = USER_MODEL.objects.all()
    serializer_class = serializers.UserSerializer

    def post(self, request, **kwargs):
        old_password = request.data['old_password']
        user = authenticate(
            request,
            username=request.user.username,
            password=old_password
        )
        if user is None:
            return Response({'error': 'User does not exist'})
        
        password1 = request.data['password1']
        password2 = request.data['password2']

        if password1 != password2:
            pass
            
        if password1 == old_password:
            pass

        user.set_password(password1)
        user.save()
        update_session_auth_hash(request, user)
        return Response({'state': True})


# class AddNewAddress(GenericAPIView):
#     queryset = USER_PROFILE_MODEL.objects.all()
#     serializer_class = serializers.AddressSerializer

#     def post(self, request, **kwargs):
#         user = request.user
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         try:
#             address = user.myuserprofile.addresses.create(**serializer.data)
#         except:
#             return Response({'error': 'Address was not created'}, status=status.HTTP_501_NOT_IMPLEMENTED)
#         serializer = self.get_serializer(instance=address)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class UserAddresses(GenericViewSet, ListModelMixin):
#     queryset = Address.objects.all()
#     serializer_class = serializers.AddressSerializer


# class DeleteAddress(GenericViewSet, DestroyModelMixin):
#     queryset = Address.objects.all()
#     serializer_class = serializers.AddressSerializer



# class AddressesViewset(GenericAPIView):
#     http_method_names = ['post', 'patch', 'options']
#     queryset = Address.objects.all()
#     serializer_class = serializers.AddressValidationSerializer

#     def post(self, request, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.create(
#             user=request.user, 
#             validated_data=serializer.validated_data
#         )
#         return Response(serializer.data)


#     # def update(self, request, **kwargs):
#     #     pass

#     def patch(self, request, **kwargs):
#         user = request.user
#         candidates = user.myuserprofile.addresses.filter(
#             id=request.data['id']
#         )
#         try:
#             address = candidates.get()
#         except:
#             return Response({'error': 'Change was not made'})

#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         new_address = serializer.update(
#             instance=address, 
#             validated_data=serializer.validated_data
#         )
#         serialized_address = self.get_serializer(instance=new_address)
#         return Response(serialized_address.data)




class ChangePersonalDetails(GenericAPIView):
    http_method_names = ['post', 'patch']
    # Dynamically update the data depending 
    # on the incoming position that was
    # included in the incoming POST data
    serializer_classes = [
        serializers.UserValidationSerializer
    ]

    def post(self, request, **kwargs):
        serializer_position = request.data.get('position', None)
        if serializer_position is not None:
            serializer_position = int(serializer_position)
        else:
            return Response({'error': 'An error occured - PF1'})
            
        content = request.data['content']
        if not content or content is None:
            return Response({}, status=status.HTTP_202_ACCEPTED)

        serializer = self._get_serializer(serializer_position, content)
        serializer.update(request.user, serializer._validated_data)
        return Response(serializer.data)

    def _get_serializer(self, position, data):
        serializer = self.serializer_classes[position]
        instance = serializer(data=data)
        instance.is_valid(raise_exception=True)
        return instance




def not_authorized_response(request):
    return Response({'error': 'Not authorized'}, status=status.HTTP_401_UNAUTHORIZED)


class AddressesApi(GenericViewSet, ListModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin):
    queryset = Address.objects.all()
    serializer_class = serializers.AddressSerializer
    permission_classes = [CustomIsAuthenticated]

    def _user_addresses(self, request):
        return self.queryset.filter(myuserprofile__id=request.user.id)

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
        queryset = self._user_addresses(request)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer, request):
        new_address = serializer.save()
        user_profile = get_object_or_404(USER_PROFILE_MODEL, id=request.user.id)
        user_profile.addresses.add(new_address)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, request)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


@api_view(['post', 'patch'])
def change_personal_details(request):
    if not check_user_token(request):
        return not_authorized_response(request)

    serializer_classes = [
        serializers.UserValidationSerializer
    ]

    def _get_serializer(position, data):
        serializer = serializer_classes[position]
        instance = serializer(data=data)
        instance.is_valid(raise_exception=True)
        return instance

    serializer_position = request.data.get('position', None)
    if serializer_position is not None:
        serializer_position = int(serializer_position)
    else:
        return Response({'error': 'An error occured - PF1'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    content = request.data['content']
    if not content or content is None:
        return Response({}, status=status.HTTP_202_ACCEPTED)

    serializer = _get_serializer(serializer_position, content)
    serializer.update(request.user, serializer._validated_data)
    return Response(serializer.data)


@api_view(['post'])
def update_preferences(request):
    if not check_user_token(request):
        return not_authorized_response(request)
    return Response({'status': 'Great'})


@api_view(['get'])
def refresh_user_details(request):
    if not check_user_token(request):
        return not_authorized_response(request)
    
    user_profile = get_object_or_404(MyUserProfile.objects.all(), id=request.user.id)
    serializer = serializers.MyUserProfileSerializer(instance=user_profile)
    return Response(serializer.data)
