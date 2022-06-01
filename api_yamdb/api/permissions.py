from rest_framework import permissions


class IsAdminPermission(permissions.BasePermission):
    '''Права доступа суперюзер или админ'''
    def has_permission(self, request, view):
        return (request.user.is_authenticated and
                request.user.is_admin)
