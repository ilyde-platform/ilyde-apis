# encoding: utf-8
#
# Copyright (c) 2020-2021 Hopenly srl.
#
# This file is part of Ilyde.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

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
