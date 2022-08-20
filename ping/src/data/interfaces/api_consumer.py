from typing import Dict, Tuple, Type
from abc import ABC, abstractmethod

class ApiConsumerInterface(ABC):

    @abstractmethod
    def get_ok_message(self) -> Tuple[int, Type[any], Dict]: pass
