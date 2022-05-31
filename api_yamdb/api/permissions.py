from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

from django.conf import settings

class RoleBasedPermission (permissions.BasePermission):
    def __init__(self):
        allowed_user_roles = None
    
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role in self.allowed_user_roles
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return request.user.role in self.allowed_user_roles
        return False


class AdminPermission(RoleBasedPermission):
    def __init__(self):
        self.allowed_user_roles = (settings.ADMIN, settings.SUPERUSER,)

    
class UserPermission(RoleBasedPermission):
    def __init__(self):
        self.allowed_user_roles = (settings.USER,)
    

class ModeratorPermission(RoleBasedPermission):
    def __init__(self):
        self.allowed_user_roles = (settings.MODERATOR,)
