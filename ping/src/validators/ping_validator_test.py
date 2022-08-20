# pylint: disable=bare-except
# pylint: disable=comparison-of-constants
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from .ping_validator import ping_validator


class MockRequest():
    def __init__(self) -> None:
        self.json = None
        


def test_ping_validator():
    request = MockRequest()
    request.json = {
        "message": "PING"
    }

    try:
        ping_validator(request)
    except:
        assert False


def test_user_register_validator_with_error():
    request = MockRequest()
    request.json = {}

    try:
        ping_validator(request)
        assert False
    except Exception as exception:
        assert isinstance(exception, HttpUnprocessableEntityError)
