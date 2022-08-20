
from requests import Request
from src.data.interfaces.api_consumer import ApiConsumerInterface
from src.domain.use_cases.ping import Ping as PingInterface
from typing import Dict, Tuple, Type


class Ping(PingInterface):
    def __init__(self, api_consumer: ApiConsumerInterface) -> None:
        self.__api_consumer = api_consumer


    def send_message(self) -> Tuple[int, Type[Request], Dict]:
        api_consumer = self.__api_consumer.get_ok_message()
        return api_consumer
