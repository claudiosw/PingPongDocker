from .api_consumer import ApiConsumer


def test_get_ok_message(requests_mock):
    requests_mock.get('http://localhost:5000/v1/pong/', status_code=200, json={ "data": { "message": "PONG" } })

    api_consumer = ApiConsumer()

    request_response = api_consumer.get_ok_message()

    assert request_response.request.method == 'GET'
    assert request_response.request.url == 'http://localhost:5000/v1/pong/'

    assert request_response.status_code == 200
    assert "message" in request_response.response["data"]
