from typing import Dict
from abc import ABC, abstractmethod


class Pong(ABC):

    @abstractmethod
    def send_message(self) -> Dict:
        pass
