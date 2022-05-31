from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

from django.conf import settings

class RoleBasedPermission (permissions.BasePermission):
    def __init__(self):
        allowed_user_roles = None
    
    def has_permission(self, request, view):
        print (self.allowed_user_roles)
        if request.user.is_authenticated:
            return (request.user.role in self.allowed_user_roles or
                    request.user.is_superuser)
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return (request.user.role in self.allowed_user_roles or 
                    request.user.is_superuser)
        return False


class AdminPermission(RoleBasedPermission):
    def __init__(self):
        self.allowed_user_roles = (settings.ROLES['admin'],)

    
class UserPermission(RoleBasedPermission):
    def __init__(self):
        self.allowed_user_roles = (settings.ROLES['user'],)
    

class ModeratorPermission(RoleBasedPermission):
    def __init__(self):
        self.allowed_user_roles = (settings.ROLES['moderator'],)
