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
