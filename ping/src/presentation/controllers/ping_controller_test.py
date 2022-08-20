from src.data.tests.ping import PingSpy
from src.presentation.http_types.http_response import HttpResponse
from .ping_controller import PingController


class HttpRequestMock():
    def __init__(self) -> None:
        self.body = {
            "message": "PING"
        }

def test_handler():
    http_request_mock = HttpRequestMock()
    use_case = PingSpy()
    ping_controller = PingController(use_case)

    response = ping_controller.handle(http_request_mock)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"] is not None
