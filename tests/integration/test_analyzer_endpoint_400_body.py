import requests
import json
from tests import fake_constants_service as fct
import os

# Get current Flask app host
host = os.getenv('SENTIMENT_ANALYSIS_HOST')

# Get current Flask app port
port = os.getenv('FLASK_RUN_PORT')


def test_none_json_body_returns_400_none_json_request_body_message():
    """
    Test if sending a request with None JSON body to the analyzer endpoint route
    results in the expected 400 Bad Request response message.
    """
    expected_response_message = fct.get_none_json_request_body_message()
    expected_body = {fct.get_response_message_key(): expected_response_message}
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    invalid_input = json.dumps(None)
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=invalid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_body


def test_missing_json_content_type_headers_returns_400_none_json_request_body_message():
    """
    Test if sending a request with valid JSON body
    and missing content type application/json headers to the analyzer endpoint route
    results in the expected 400 Bad Request response message.
    """
    expected_response_message = fct.get_none_json_request_body_message()
    expected_body = {fct.get_response_message_key(): expected_response_message}
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: 'x'})
    response = requests.post(url, data=valid_input)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_body


def test_empty_json_body_returns_400_missing_input_key_body_message():
    """
    Test if sending a request with empty JSON body to the analyzer endpoint route
    results in the expected 400 Bad Request response message.
    """
    expected_response_message = fct.get_missing_input_key_message()
    expected_body = {fct.get_response_message_key(): expected_response_message}
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    invalid_input = json.dumps({})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=invalid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_body


def test_invalid_json_key_returns_400_missing_input_key_body_message():
    """
    Test if sending a request with missing "input" key to the analyzer endpoint route
    results in the expected 400 Bad Request response message.
    """
    expected_response_message = fct.get_missing_input_key_message()
    expected_body = {fct.get_response_message_key(): expected_response_message}
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    invalid_input = json.dumps({'invalid_key': 'x'})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=invalid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_body


def test_none_json_input_key_returns_400_none_input_key_body_message():
    """
    Test if sending a request with None "input" key to the analyzer endpoint route
    results in the expected 400 Bad Request response message.
    """
    expected_response_message = fct.get_none_input_key_message()
    expected_body = {fct.get_response_message_key(): expected_response_message}
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    invalid_input = json.dumps({input_key: None})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=invalid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_body


def test_too_big_json_input_returns_400_too_big_input_length_body_message():
    """
    Test if sending a request with too big "input" key to the analyzer endpoint route
    results in the expected 400 Bad Request response message.
    """
    expected_response_message = fct.get_too_big_input_length_message()
    expected_body = {fct.get_response_message_key(): expected_response_message}
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    invalid_input = json.dumps({input_key: 'x' * (fct.get_max_input_length() + 1)})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=invalid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_body