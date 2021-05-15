from rest_framework import permissions


class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow admin user
        if request.user.is_superuser or request.user.is_staff:
            return True

        # Write permissions are only allowed to the user itself
        return obj == request.user
