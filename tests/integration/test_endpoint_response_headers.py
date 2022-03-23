import requests
import json
from tests import fake_constants_service as fct
import os

# Get current Flask app host
host = os.getenv('SENTIMENT_ANALYSIS_HOST')

# Get current Flask app port
port = os.getenv('FLASK_RUN_PORT')


index_endpoint_expected_headers = {
    'Content-Type': fct.get_index_content_type(),
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Methods': 'GET,POST',
    'Access-Control-Allow-Origin': '*'
}

analyzer_endpoint_expected_headers = {
    'Content-Type': fct.get_application_content_type(),
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Methods': 'GET,POST',
    'Access-Control-Allow-Origin': '*'
}


def test_analyzer_endpoint_200_headers():
    """
    Test if sending a regular request to the analyzer endpoint route
    results in the expected headers.
    """
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: 'x'})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    assert analyzer_endpoint_expected_headers.items() <= response.headers.items()


def test_none_json_body_400_headers():
    """
    Test if sending a request with None JSON body to the analyzer endpoint route
    results in the expected headers.
    """
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    invalid_input = json.dumps(None)
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=invalid_input, headers=headers)
    assert analyzer_endpoint_expected_headers.items() <= response.headers.items()


def test_empty_json_body_400_headers():
    """
    Test if sending a request with empty JSON body to the analyzer endpoint route
    results in the expected headers.
    """
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    invalid_input = json.dumps({})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=invalid_input, headers=headers)
    assert analyzer_endpoint_expected_headers.items() <= response.headers.items()


def test_missing_json_content_type_headers_400_headers():
    """
    Test if sending a request with valid JSON body
    and missing content type application/json headers to the analyzer endpoint route
    results in the expected headers.
    """
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: 'x'})
    response = requests.post(url, data=valid_input)
    assert analyzer_endpoint_expected_headers.items() <= response.headers.items()


def test_invalid_json_key_400_headers():
    """
    Test if sending a request with missing "input" key to the analyzer endpoint route
    results in the expected headers.
    """
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    invalid_input = json.dumps({'invalid_key': 'x'})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=invalid_input, headers=headers)
    assert analyzer_endpoint_expected_headers.items() <= response.headers.items()


def test_none_json_input_key_400_headers():
    """
    Test if sending a request with None "input" key to the analyzer endpoint route
    results in the expected headers.
    """
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    invalid_input = json.dumps({input_key: None})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=invalid_input, headers=headers)
    assert analyzer_endpoint_expected_headers.items() <= response.headers.items()


def test_too_big_json_input_400_headers():
    """
    Test if sending a request with too big "input" key to the analyzer endpoint route
    results in the expected headers.
    """
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    invalid_input = json.dumps({input_key: 'x' * (fct.get_max_input_length() + 1)})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=invalid_input, headers=headers)
    assert analyzer_endpoint_expected_headers.items() <= response.headers.items()


def test_max_length_json_input_200_headers():
    """
    Test if sending a request with biggest possible "input" key to the analyzer endpoint route
    results in the expected headers.
    """
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: 'x' * fct.get_max_input_length()})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    assert analyzer_endpoint_expected_headers.items() <= response.headers.items()


def test_index_endpoint_200_headers():
    """
    Test if sending a regular request to the index endpoint route
    results in the expected headers.
    """
    url_prefix = fct.get_index_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    response = requests.get(url)
    assert index_endpoint_expected_headers.items() <= response.headers.items()