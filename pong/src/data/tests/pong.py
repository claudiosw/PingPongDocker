from typing import Dict

class PongSpy:
    def __init__(self) -> None:
        pass

    def find_by_name(self, name: str) -> Dict:
        return {
            "data": {
                "message": 'PONG'
            }
        }
