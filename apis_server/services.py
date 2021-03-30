# encoding: utf-8
import grpc
from elasticsearch import Elasticsearch
from flask import current_app
from minio import Minio
from keycloak.realm import KeycloakRealm
from mlflow.tracking import MlflowClient

from protos import dataset_pb2_grpc, project_pb2_grpc, job_pb2_grpc


def get_minio_client():

    # minio client
    client = Minio(current_app.config.get('MINIO_HOST'), access_key=current_app.config.get('AWS_ACCESS_KEY_ID'),
                   secret_key=current_app.config.get('AWS_SECRET_ACCESS_KEY'), secure=False)
    return client


def get_datasets_services_stub():
    channel = grpc.insecure_channel(current_app.config.get('DATASETS_SERVICES_ENDPOINT'))
    stub = dataset_pb2_grpc.DatasetServicesStub(channel=channel)
    return stub


def get_projects_services_stub():
    channel = grpc.insecure_channel(current_app.config.get("PROJECTS_SERVICES_ENDPOINT"))
    stub = project_pb2_grpc.ProjectServicesStub(channel=channel)
    return stub


def get_environments_services_stub():
    channel = grpc.insecure_channel(current_app.config.get("JOBS_SERVICES_ENDPOINT"))
    stub = job_pb2_grpc.EnvironmentServicesStub(channel=channel)
    return stub


def get_workspaces_services_stub():
    channel = grpc.insecure_channel(current_app.config.get("JOBS_SERVICES_ENDPOINT"))
    stub = job_pb2_grpc.WorkspaceServicesStub(channel=channel)
    return stub


def get_modelapis_services_stub():
    channel = grpc.insecure_channel(current_app.config.get("JOBS_SERVICES_ENDPOINT"))
    stub = job_pb2_grpc.ModelApisServicesStub(channel=channel)
    return stub


def get_runs_services_stub():
    channel = grpc.insecure_channel(current_app.config.get("JOBS_SERVICES_ENDPOINT"))
    stub = job_pb2_grpc.RunServicesStub(channel=channel)
    return stub


def get_experiments_services_stub():
    channel = grpc.insecure_channel(current_app.config.get("JOBS_SERVICES_ENDPOINT"))
    stub = job_pb2_grpc.ExperimentServicesStub(channel=channel)
    return stub


def get_keycloak_users(server_url):
    realm = KeycloakRealm(server_url=server_url,
                          realm_name=current_app.config.get('KEYCLOAK_REALM'))
    oidc_client = realm.open_id_connect(client_id=current_app.config.get('KEYCLOAK_CLIENT_ID'),
                                        client_secret=current_app.config.get('KEYCLOAK_CLIENT_SECRET'))
    credentials = oidc_client.client_credentials()
    admin_client = realm.admin.set_token(credentials.get("access_token"))

    return admin_client.realms.by_name(current_app.config.get('KEYCLOAK_REALM')).users


def get_mlflow_client():
    client = MlflowClient(tracking_uri=current_app.config.get("MLFLOW_TRACKING_URI"))
    return client


def query_elasticsearch(query: str):
    es = Elasticsearch(hosts=[current_app.config.get("ELASTICSEARCH_HOST")])
    res = es.search(index="_all", body={"query": {"match": {
        "kubernetes.pod_name": {
            "query": query,
        }
    }}}, size=1000)

    data = [{"timestamp": hit['_source']['@timestamp'], "message": hit['_source']['log'],
             "source": hit['_source']['kubernetes']["pod_name"]}
            for hit in res['hits']['hits'] if query in hit['_source']['kubernetes']["pod_name"]]
    payload = {
        "total": len(data),
        "data": data
    }
    return payload
