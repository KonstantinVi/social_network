"""Private api version 1."""

from flask import Blueprint

private_api_v1 = Blueprint('private_api_v1', __name__)


@private_api_v1.route('/hello', methods=['GET'])
def hello():
    return "Hello from Open API v1"
