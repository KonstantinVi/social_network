"""Open api version 1."""

from flask import Blueprint

open_api_v1 = Blueprint('open_api_v1', __name__)


# /api/v1/open/hello
@open_api_v1.route('/hello', methods=['GET'])
def hello():
    return "Hello from Open API v1"
