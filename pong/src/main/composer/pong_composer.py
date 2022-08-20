from src.data.use_cases.pong import Pong
from src.presentation.controllers.pong_controller import PongController


def pong_composer():
    use_case = Pong()
    controller = PongController(use_case)

    return controller
 