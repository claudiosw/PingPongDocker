from collections import namedtuple
import requests


def create_mock_api_consumer():
    api_named_tuple = namedtuple('GET_Ok', 'status_code request response')
    req = requests.Request(
        method='GET',
        url='http://localhost:5000/v1/pong'
    )

    response = {
        'data': {
            'message': 'PONG'
        }
    }
    status_code = 200

    return api_named_tuple(
        status_code=status_code, request=req, response=response
    )
