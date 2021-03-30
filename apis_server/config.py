# coding: utf-8

import os
from decouple import config
from pathlib import Path

_HERE = os.path.dirname(__file__)


class APIConfig(object):
    BASE_DIR = Path(_HERE).parent
    SECRET_KEY = 'Ki72CLxzQgLzJt7trCUltwk1VD7bXKr7cDiYxjI9J_U='
    KEYCLOAK_CLIENT_ID = "ilyde"
    KEYCLOAK_CLIENT_SECRET = "017abcc3-222c-424d-b6f6-96468d977bea"
    KEYCLOAK_REALM = "IlydeRealm"

    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')

    MINIO_HOST = config('MINIO_HOST')
    MINIO_ENDPOINT = config('MINIO_ENDPOINT')

    MLFLOW_TRACKING_URI = config("MLFLOW_TRACKING_URI")
    MLFLOW_S3_ENDPOINT_URL = config("MLFLOW_S3_ENDPOINT_URL")

    # Protocol buffers endpoint
    DATASETS_SERVICES_ENDPOINT = config("DATASETS_SERVICES_ENDPOINT")
    PROJECTS_SERVICES_ENDPOINT = config("PROJECTS_SERVICES_ENDPOINT")
    JOBS_SERVICES_ENDPOINT = config("JOBS_SERVICES_ENDPOINT")

    # ETCD
    ETCD_PORT = 2379
    ETCD_HOST = config("ETCD_HOST")

    # ELASTICSEARCH
    ELASTICSEARCH_HOST = config("ELASTICSEARCH_HOST")


