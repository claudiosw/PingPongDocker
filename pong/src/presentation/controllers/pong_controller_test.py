from src.data.tests.pong import PongSpy
from src.presentation.http_types.http_response import HttpResponse
from .pong_controller import PongController


class HttpRequestMock():
    def __init__(self) -> None:
        pass


def test_handler():
    http_request_mock = HttpRequestMock()
    use_case = PongSpy()
    pong_controller = PongController(use_case)

    response = pong_controller.handle(http_request_mock)

    assert use_case.find_by_id_attributes["id"] == http_request_mock.path_params["id"]

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"] is not None
