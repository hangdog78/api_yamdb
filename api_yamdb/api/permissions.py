from rest_framework import permissions


class IsAdminPermission(permissions.BasePermission):
    '''Права доступа суперюзер или админ'''
    def has_permission(self, request, view):
        return (request.user.is_authenticated
                and request.user.is_admin)


class IsAdminOrReadOnly(permissions.BasePermission):
    '''Права доступа админ или только просмотр'''
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role == 'admin'
