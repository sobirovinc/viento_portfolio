from rest_framework.permissions import BasePermission


class AllowAnyPermission(BasePermission):
    def has_permission(self, request, view):
        return True
