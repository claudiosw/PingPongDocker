from requests import Request
from typing import Dict, Tuple, Type
from abc import ABC, abstractmethod


class Ping(ABC):

    @abstractmethod
    def send_message(self) -> Tuple[int, Type[Request], Dict]:
        pass
