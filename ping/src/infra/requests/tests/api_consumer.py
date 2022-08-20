from typing import Dict, Tuple, Type
from requests import Request
from src.domain.tests.api_consumer import create_mock_api_consumer


class ApiConsumerSpy:
    def __init__(self) -> None:
        pass

    def get_ok_message() -> Tuple[int, Type[Request], Dict]:
        return create_mock_api_consumer()
