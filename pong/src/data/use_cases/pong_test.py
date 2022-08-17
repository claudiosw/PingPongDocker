from .pong import Pong


def test_pong():
    response = Pong.send_message()

    assert "data" in response
    assert response['data']['message'] == 'PONG'
