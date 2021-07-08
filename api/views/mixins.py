from rest_framework.permissions import IsAuthenticated, IsAdminUser


class GlobalAPIMixins:
    @classmethod
    def get_extra_actions(self, **kwargs):
        return []


class RestrictedGlobalAPIMixin(GlobalAPIMixins):
    authentication_classes = []
    permission_classes = []
