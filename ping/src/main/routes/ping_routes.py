from flask import Blueprint, jsonify, request
from src.main.adapters.request_adapter import request_adapter
from src.main.composer.ping_composer import ping_composer
from src.presentation.error_handler.error_controller import handle_errors
from src.validators.ping_validator import ping_validator


ping_routes_bp = Blueprint("ping_routes", __name__)


@ping_routes_bp.route("/v1/ping/", methods=["POST"])
def get_ping():
    http_response = None

    try:
        ping_validator(request)
        http_response = request_adapter(request, ping_composer().handle)
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code
