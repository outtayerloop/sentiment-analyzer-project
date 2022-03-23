import requests
import json
from tests import fake_constants_service as fct
import os

# Get current Flask app host
host = os.getenv('SENTIMENT_ANALYSIS_HOST')

# Get current Flask app port
port = os.getenv('FLASK_RUN_PORT')


def test_analyzer_endpoint_is_up_and_running():
    """
    Test if sending a regular request to the analyzer endpoint route
    results in a 200 OK response.
    """
    expected_status_code = 200
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: 'x'})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    assert response.status_code == expected_status_code


def test_analyzer_endpoint_get_request_returns_405():
    """
    Test if sending a regular GET request to the analyzer endpoint route
    results in a 405 Method Not Allowed response.
    """
    expected_status_code = 405
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: 'x'})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.get(url, data=valid_input, headers=headers)
    assert response.status_code == expected_status_code


def test_analyzer_endpoint_put_request_returns_405():
    """
    Test if sending a regular PUT request to the analyzer endpoint route
    results in a 405 Method Not Allowed response.
    """
    expected_status_code = 405
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: 'x'})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.put(url, data=valid_input, headers=headers)
    assert response.status_code == expected_status_code


def test_analyzer_endpoint_delete_request_returns_405():
    """
    Test if sending a regular DELETE request to the analyzer endpoint route
    results in a 405 Method Not Allowed response.
    """
    expected_status_code = 405
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: 'x'})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.delete(url, data=valid_input, headers=headers)
    assert response.status_code == expected_status_code


def test_none_json_body_returns_400():
    """
    Test if sending a request with None JSON body to the analyzer endpoint route
    results in a 400 Bad Request response.
    """
    expected_status_code = 400
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    invalid_input = json.dumps(None)
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=invalid_input, headers=headers)
    assert response.status_code == expected_status_code


def test_empty_json_body_returns_400():
    """
    Test if sending a request with empty JSON body to the analyzer endpoint route
    results in a 400 Bad Request response.
    """
    expected_status_code = 400
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    invalid_input = json.dumps({})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=invalid_input, headers=headers)
    assert response.status_code == expected_status_code


def test_missing_json_content_type_headers_returns_400():
    """
    Test if sending a request with valid JSON body
    and missing content type application/json headers to the analyzer endpoint route
    results in a 400 Bad Request response.
    """
    expected_status_code = 400
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: 'x'})
    response = requests.post(url, data=valid_input)
    assert response.status_code == expected_status_code


def test_invalid_json_key_returns_400():
    """
    Test if sending a request with missing "input" key to the analyzer endpoint route
    results in a 400 Bad Request response.
    """
    expected_status_code = 400
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    invalid_input = json.dumps({'invalid_key': 'x'})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=invalid_input, headers=headers)
    assert response.status_code == expected_status_code


def test_none_json_input_key_returns_400():
    """
    Test if sending a request with None "input" key to the analyzer endpoint route
    results in a 400 Bad Request response.
    """
    expected_status_code = 400
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    invalid_input = json.dumps({input_key: None})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=invalid_input, headers=headers)
    assert response.status_code == expected_status_code


def test_too_big_json_input_returns_400():
    """
    Test if sending a request with too big "input" key to the analyzer endpoint route
    results in a 400 Bad Request response.
    """
    expected_status_code = 400
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    invalid_input = json.dumps({input_key: 'x' * (fct.get_max_input_length() + 1)})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=invalid_input, headers=headers)
    assert response.status_code == expected_status_code


def test_max_length_json_input_returns_200():
    """
    Test if sending a request with biggest possible "input" key to the analyzer endpoint route
    results in a 200 OK response.
    """
    expected_status_code = 200
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: 'x' * fct.get_max_input_length()})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    assert response.status_code == expected_status_code


def test_index_endpoint_is_up_and_running():
    """
    Test if sending a regular request to the index endpoint route
    results in a 200 OK response.
    """
    expected_status_code = 200
    url_prefix = fct.get_index_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    response = requests.get(url)
    assert response.status_code == expected_status_code


def test_index_endpoint_post_request_returns_405():
    """
    Test if sending a regular POST request to the index endpoint route
    results in a 405 Method Not Allowed response.
    """
    expected_status_code = 405
    url_prefix = fct.get_index_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    response = requests.post(url)
    assert response.status_code == expected_status_code


def test_index_endpoint_put_request_returns_405():
    """
    Test if sending a regular PUT request to the index endpoint route
    results in a 405 Method Not Allowed response.
    """
    expected_status_code = 405
    url_prefix = fct.get_index_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    response = requests.put(url)
    assert response.status_code == expected_status_code


def test_index_endpoint_delete_request_returns_405():
    """
    Test if sending a regular DELETE request to the index endpoint route
    results in a 405 Method Not Allowed response.
    """
    expected_status_code = 405
    url_prefix = fct.get_index_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    response = requests.delete(url)
    assert response.status_code == expected_status_code


