from typing import Dict, Tuple, Type
from requests import Request
from src.domain.tests.api_consumer import create_mock_api_consumer


class PingSpy:

    def send_message(self) -> Tuple[int, Type[Request], Dict]:
        return create_mock_api_consumer()
