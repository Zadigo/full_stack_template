from rest_framework.permissions import BasePermission


class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)
        # if has_user:
        #     can_view_profile = request.user.has_perm('profile.can_view')
        #     return all([can_view_profile, has_user])


class RequiresAdmin(IsAuthenticated):
    def has_permission(self, request, view):
        has_user = super().has_permission(request, view)
        return all([has_user, request.user.is_admin or request.user.is_staff])


class HasPermissions(BasePermission):
    def has_permission(self, request, view):
        return True
        # return request.user.has_perms(['profile.edit'])
