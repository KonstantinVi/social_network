"""Partner api version 1."""

from flask import Blueprint

partner_api_v1 = Blueprint('partner_api_v1', __name__)


# /api/v1/partner/hello
@partner_api_v1.route('/hello', methods=['GET'])
def hello():
    return "Hello from Partner API v1"
