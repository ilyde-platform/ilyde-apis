import connexion
import six

from apis_server.decorators import catch_exception, check_permissions
from apis_server.permissions import IsAdmin
from apis_server.serializers import ErrorSerializer, StatusSerializer, PageLimitListSerializer
from apis_server.serializers.user_serializer import UserSerializer
from apis_server import util
from apis_server.services import get_keycloak_users


def format_groups(groups):
    return [g.get("name") for g in groups]


def get_keycloak_server_url():
    server_url = connexion.request.headers["Host"] if not connexion.request.headers.get("X-Forwarded-Host") \
        else connexion.request.headers["X-Forwarded-Host"]
    server_scheme = connexion.request.scheme if not connexion.request.headers.get("X-Forwarded-Proto") \
        else connexion.request.headers["X-Forwarded-Proto"]

    return "{}://{}".format(server_scheme, server_url)


@catch_exception
@check_permissions(permissions=[IsAdmin])
def create_user(body, **kwargs):
    """Create a user
    :param body: User object to be created
    :type body: dict | bytes

    :rtype: UserSerializer
    """
    serializer = UserSerializer.from_dict(body)
    # create user
    server_url = get_keycloak_server_url()
    users = get_keycloak_users(server_url)
    users.create(serializer.username,
                 first_name=serializer.first_name,
                 last_name=serializer.last_name,
                 enabled=True,
                 groups=serializer.groups,
                 email=serializer.email,
                 email_verified=True,
                 )
    # set temporary password
    all_users = users.all()
    user_id = None
    created_at = None
    for u in all_users:
        if u.get("username") == serializer.username:
            user_id = u.get("id")
            created_at = u.get("createdTimestamp")

    users.by_id(user_id=user_id).reset_password(serializer.password, temporary=True)
    serializer.id = user_id
    serializer.email_verified = True
    serializer.enabled = True
    serializer.created_timestamp = str(created_at)

    return serializer


@catch_exception
@check_permissions(permissions=[IsAdmin])
def delete_user(id_, **kwargs):
    """Delete a user
    :param id_: The ID of the user object to be deleted
    :type id_: str

    :rtype: StatusSerializer
    """
    server_url = get_keycloak_server_url()
    users = get_keycloak_users(server_url)
    user = users.by_id(id_)
    user.update(enabled=False)

    return StatusSerializer(status=200, message="User successfully deleted.")


@catch_exception
def list_users(**kwargs):
    """list users
    :rtype: PageLimitListSerializer
    """
    server_url = get_keycloak_server_url()
    users = get_keycloak_users(server_url)
    users_all = users.all()

    data = [UserSerializer(
        id=user.get("id"),
        username=user.get("username"),
        first_name=user.get("firsName"),
        last_name=user.get("lastName"),
        enabled=user.get("enabled"),
        groups=format_groups(users.by_id(user.get("id")).groups.all()),
        email=user.get("email"),
        email_verified=user.get("emailVerified"),
        created_timestamp=str(user.get("createdTimestamp"))
    ) for user in users_all]

    return PageLimitListSerializer(data=data, total=len(data))


@catch_exception
@check_permissions(permissions=[IsAdmin])
def retrieve_user(id_, **kwargs):
    """Retrieve a user
    :param id_: The ID of the user object to be retrieved
    :type id_: str
    :rtype: UserSerializer
    """
    server_url = get_keycloak_server_url()
    users = get_keycloak_users(server_url)
    user = users.by_id(id_)
    user_detail = user.get()

    return UserSerializer(
        id=user.u,
        username=user_detail.get("username"),
        first_name=user_detail.get("firsName"),
        last_name=user_detail.get("lastName"),
        enabled=user_detail.get("enabled"),
        email=user_detail.get("email"),
        groups=format_groups(user.groups.all()),
        email_verified=user_detail.get("emailVerified"),
        created_timestamp=str(user_detail.get("createdTimestamp"))
    )


@catch_exception
@check_permissions(permissions=[IsAdmin])
def update_user(id_, body, **kwargs):
    """Update a user
    :param id_: The ID of the user object to be updated
    :type id_: str
    :param body: User object to be updated
    :type body: dict | bytes

    :rtype: UserSerializer
    """
    serializer = UserSerializer.from_dict(body)
    server_url = get_keycloak_server_url()
    users = get_keycloak_users(server_url)
    user = users.by_id(id_)
    user.update(**body)

    return serializer
