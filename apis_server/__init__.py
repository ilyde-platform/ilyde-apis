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
import json
from flask import Response
import connexion
from flask_cors import CORS

from apis_server import encoder
from apis_server.serializers import ErrorSerializer
from apis_server import config


options = {"swagger_ui": True}
app = connexion.App(__name__, specification_dir='./openapi/', options=options)
app.app.json_encoder = encoder.JSONEncoder
app.add_api('openapi.yaml', arguments={'title': 'Ilyde Apis'}, pythonic_params=True)

# load config
app.app.config.from_object(config.APIConfig)

# add CORS support
CORS(app.app)


@app.app.after_request
def rewrite_response(response: Response):
    if response.status_code >= 400:
        if response.data.decode('utf-8').find('"type":') is not None:
            original = json.loads(response.data.decode('utf-8'))
            response.data = json.dumps(ErrorSerializer(status=original['status'],
                                                       title=original['title'], detail=original['detail']).to_dict())
    return response
