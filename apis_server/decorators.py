# encoding: utf-8

from typing import List
from apis_server.errors import handle_exceptions
from apis_server.serializers import ErrorSerializer


def catch_exception(function):
    def inner(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as e:
            handle_exceptions(e)

    return inner


def check_permissions(permissions: List):
    """
    check global permissions
    :param permissions: permissions to check for this resource
    :return:
    """
    def inner(func):
        def wrapper(*args, **kwargs):
            if all([permission.has_permission(kwargs["token_info"]) for permission in permissions]):
                return func(*args, **kwargs)

            return ErrorSerializer(status=403, title="Permission Denied",
                                   detail="You don't have enough permission to access this content."), 403
        return wrapper
    return inner
