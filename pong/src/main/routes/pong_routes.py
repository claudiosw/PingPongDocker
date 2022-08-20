from flask import Blueprint, jsonify, request
from src.main.adapters.request_adapter import request_adapter
from src.main.composer.pong_composer import pong_composer
from src.presentation.error_handler.error_controller import handle_errors

pong_routes_bp = Blueprint("pong_routes", __name__)


@pong_routes_bp.route("/v1/pong/", methods=["GET"])
def get_pong():
    http_response = None

    try:
        http_response = request_adapter(request, pong_composer().handle)
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code
