from src.infra.requests.tests.api_consumer import ApiConsumerSpy
from .ping import Ping


def test_ping():
    api_consumer = ApiConsumerSpy
    ping = Ping(api_consumer)
    response = ping.send_message()

    assert "data" in response[2]
    assert response[2]['data']['message'] == 'PONG'
