# -*- coding: utf-8 -*-
import logging

import connexion
import grpc
from minio import ResponseError
from mlflow.exceptions import MlflowException

# setup logger
FORMAT = '%(asctime)s %(levelname)s %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger(__name__)

minio_status_dict = {
    'PermanentRedirect': 301,
    'Redirect': 307,
    'BadRequest': 400,
    'AccessDenied': 403,
    'NoSuchKey': 404,
    'NoSuchBucket': 404,
    'MethodNotAllowed': 405,
    'Conflict': 409,
    'InternalError': 500,
    'UnknownException': 500,
}


def handle_exceptions(exception):
    logger.error(exception)
    if isinstance(exception, grpc.RpcError):
        status_code = exception.code()
        # want to do some specific action based on the error?
        # propagate error
        if grpc.StatusCode.INVALID_ARGUMENT == status_code:
            raise connexion.ProblemException(status=400, detail="Bad request", title="API Error")

        if grpc.StatusCode.NOT_FOUND == status_code:
            return connexion.ProblemException(status=404, detail="Resource not found on server", title="API Error")

        raise connexion.ProblemException(status=500, detail="Ops!, An unexpected error occur.", title="API Error")

    elif isinstance(exception, MlflowException):
        raise connexion.ProblemException(status=exception.get_http_status_code(), detail=exception.message,
                                         title="API Error")

    elif isinstance(exception, ResponseError):
        raise connexion.ProblemException(status=minio_status_dict[exception.code], detail=exception.message,
                                         title="API Error")

    else:
        raise connexion.ProblemException(status=500, detail="Ops!, An unexpected error occur.", title="API Error")



