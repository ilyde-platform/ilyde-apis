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
import connexion
import six
from flask import current_app
from jose import JWTError
from keycloak.realm import KeycloakRealm
from werkzeug.exceptions import Unauthorized


def info_from_jwt(token):
    """
    Check and retrieve authentication information from custom bearer token.
    Returned value will be passed in 'token_info' parameter of your operation function, if there is one.
    'sub' or 'uid' will be set in 'user' parameter of your operation function, if there is one.

    :param token Token provided by Authorization header
    :type token: str
    :return: Decoded token information or None if token is invalid
    :rtype: dict | None
    """

    server_url = connexion.request.headers["Host"] if not connexion.request.headers.get("X-Forwarded-Host")\
        else connexion.request.headers["X-Forwarded-Host"]
    server_scheme = connexion.request.scheme if not connexion.request.headers.get("X-Forwarded-Proto")\
        else connexion.request.headers["X-Forwarded-Proto"]

    # Configure client
    realm = KeycloakRealm(server_url="{}://{}".format(server_scheme, server_url),
                          realm_name=current_app.config.get('KEYCLOAK_REALM'))

    oidc_client = realm.open_id_connect(client_id=current_app.config.get('KEYCLOAK_CLIENT_ID'),
                                        client_secret=current_app.config.get('KEYCLOAK_CLIENT_SECRET'))

    # Decode Token
    certs = oidc_client.certs()
    options = {"verify_signature": True, "verify_aud": True, "exp": True}

    try:
        return oidc_client.decode_token(token, key=certs, options=options)
    except JWTError as e:
        six.raise_from(Unauthorized, e)


