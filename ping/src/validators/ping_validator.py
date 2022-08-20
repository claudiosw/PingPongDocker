from cerberus import Validator
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


def ping_validator(request: any):

    request_body_validator = Validator({
        "message": {"type": "string", 'regex': 'PING', "required": True, "empty": False}
    })

    response = request_body_validator.validate(request.json)

    if response is False:
        raise HttpUnprocessableEntityError(request_body_validator.errors)
