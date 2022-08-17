from src.infra.requests.api_consumer import ApiConsumer
from src.data.use_cases.ping import Ping
from src.presentation.controllers.ping_controller import PingController


def ping_composer():
    api_consumer = ApiConsumer()
    use_case = Ping(api_consumer)
    controller = PingController(use_case)

    return controller
 