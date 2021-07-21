from rest_framework.permissions import IsAuthenticated, IsAdminUser
from api import check_user_token


class GlobalAPIMixins:
    @classmethod
    def get_extra_actions(self, **kwargs):
        return []


class RestrictedGlobalAPIMixin(GlobalAPIMixins):
    authentication_classes = []
    permission_classes = []


class CustomIsAuthenticated(IsAuthenticated):
    def has_permission(self, request, view):
        return check_user_token(request)
