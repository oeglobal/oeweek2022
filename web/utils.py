from rest_framework_jwt.utils import jwt_payload_handler
from django.contrib.auth.models import User


def custom_jwt_payload_handler(user):
    payload = jwt_payload_handler(user)

    payload['staff'] = user.is_staff
    return payload
