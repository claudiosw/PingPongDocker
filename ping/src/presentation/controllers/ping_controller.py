from typing import Type
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.domain.use_cases.ping import Ping as PingInterface


class PingController(ControllerInterface):
    def __init__(self, use_case: Type[PingInterface]) -> None:
        self.__use_case = use_case

    def handle(self, http_request: Type[HttpRequest]) -> Type[HttpResponse]:
        response = self.__use_case.send_message()

        return HttpResponse(
            status_code=200,
            body={
                "data": {
                    "type": response["data"],
                }
            }
        )
