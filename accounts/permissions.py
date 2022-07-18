from rest_framework.permissions import BasePermission

class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        has_user = bool(request.user and request.user.is_authenticated)
        if has_user:
            can_view_profile = request.user.has_perm('profile.can_view')
            return all([can_view_profile, has_user])
        return has_user


class HasPermissions(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perms(['profile.edit'])
