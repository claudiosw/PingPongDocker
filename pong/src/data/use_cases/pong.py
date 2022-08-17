from typing import Dict


class Pong():
    def __init__(self) -> None:
        self.__message = "PONG"


    def send_message(self):
        return self.__format_response()

    
    def __format_response(self) -> Dict:
        return {
            "data": {
                "message": self.__message
            }
        }
