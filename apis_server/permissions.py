# encoding: utf-8

class BasePermission:
    """
    A base class from which all permission classes should inherit.
    """

    @classmethod
    def has_permission(cls, token_info):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return True

    @classmethod
    def has_object_permission(cls, token_info, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return True


class IsAdmin(BasePermission):
    """
        Permission for Admins
    """
    @classmethod
    def has_permission(cls, token_info):
        return "manager" in token_info["groups"]


class IsProjectMember(BasePermission):
    """
        Class permission for project resources
    """
    @classmethod
    def has_permission(cls, token_info):
        return True

    @classmethod
    def has_object_permission(cls, token_info, obj):
        return token_info["sub"] in obj.members or "manager" in token_info["groups"]
