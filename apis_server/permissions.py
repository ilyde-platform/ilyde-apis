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
