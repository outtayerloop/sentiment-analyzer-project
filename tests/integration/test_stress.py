import time
import datetime

import futures3

import requests
import json

from requests import Response

from tests import fake_constants_service as fct
import os
import numpy as np

# Get current Flask app host
host = os.getenv('SENTIMENT_ANALYSIS_HOST')

# Get current Flask app port
port = os.getenv('FLASK_RUN_PORT')

# Max expected response time in milliseconds
max_response_time_threshold = 100 * 1000


def test_index_endpoint_200_response_time_when_single_request():
    """
    Test if sending single valid request to the index endpoint
    does not take longer than the max accepted 200 response time threshold.
    """
    url_prefix = fct.get_index_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    response = requests.get(url)
    response_time = response.elapsed.total_seconds() * 1000
    assert response_time <= max_response_time_threshold


def test_index_endpoint_405_response_time_when_single_request():
    """
    Test if sending single invalid request to the index endpoint
    does not take longer than the max accepted 405 response time threshold.
    """
    url_prefix = fct.get_index_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    response = requests.post(url)
    response_time = response.elapsed.total_seconds() * 1000
    assert response_time <= max_response_time_threshold


def test_analyzer_endpoint_200_response_time_when_single_request():
    """
    Test if sending single valid request to the analyzer endpoint
    does not take longer than the max accepted 200 response time threshold.
    """
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: 'x'})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    response_time = response.elapsed.total_seconds() * 1000
    assert response_time <= max_response_time_threshold


def test_analyzer_endpoint_400_response_time_when_single_request():
    """
    Test if sending single invalid request to the analyzer endpoint
    does not take longer than the max accepted 400 response time threshold.
    """
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    invalid_input = json.dumps(None)
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=invalid_input, headers=headers)
    response_time = response.elapsed.total_seconds() * 1000
    assert response_time <= max_response_time_threshold


def test_analyzer_endpoint_405_response_time_when_single_request():
    """
    Test if sending single invalid request to the analyzer endpoint
    does not take longer than the max accepted 405 response time threshold.
    """
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: 'x'})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.put(url, data=valid_input, headers=headers)
    response_time = response.elapsed.total_seconds() * 1000
    assert response_time <= max_response_time_threshold


def test_index_endpoint_stress_with_1000_requests_per_minute_for_2_minutes():
    """
    Test if sending 1000 valid requests per minute for 2 minutes to the index endpoint
    results in an average response delay inferior or equal to the max accepted one.
    """
    request_count_per_second = 100
    iteration_count = 2  # test for 2 minutes
    url_prefix = fct.get_index_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    all_responses = []
    for i in range(0, iteration_count):
        begin_time_i = datetime.datetime.now()
        next_iteration_time_i = begin_time_i + datetime.timedelta(minutes=1)
        for j in range(0, 10):  # we are going to send 100 request per second for 10 seconds
            begin_time_j = datetime.datetime.now()
            next_iteration_time_j = begin_time_j + datetime.timedelta(seconds=1)
            with futures3.ThreadPoolExecutor(max_workers=request_count_per_second) as pool:
                responses = list(pool.map(requests.get, [url] * request_count_per_second))
                all_responses = all_responses + responses
                end_time_j = datetime.datetime.now()
            if end_time_j < next_iteration_time_j:
                remaining_sleep_time_j = (next_iteration_time_j - end_time_j).total_seconds()
                time.sleep(remaining_sleep_time_j)
        end_time_i = datetime.datetime.now()
        if end_time_i < next_iteration_time_i and i < iteration_count - 1:
            remaining_sleep_time_i = (next_iteration_time_i - end_time_i).total_seconds()
            time.sleep(remaining_sleep_time_i)
    delays = list(map(lambda response: response.elapsed.total_seconds() * 1000, all_responses))
    assert np.mean(delays) <= max_response_time_threshold


def test_analyzer_endpoint_stress_with_1000_requests_per_minute_for_2_minutes():
    """
    Test if sending 1000 valid requests per minute for 2 minutes to the analyzer endpoint
    results in an average response delay inferior or equal to the max accepted one.
    """
    request_count_per_second = 100
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: 'x'})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    iteration_count = 2  # test for 2 minutes

    def do_post_to_analyzer_endpoint(current_url: str) -> Response:
        return requests.post(current_url, data=valid_input, headers=headers)

    all_responses = []
    for i in range(0, iteration_count):
        begin_time_i = datetime.datetime.now()
        next_iteration_time_i = begin_time_i + datetime.timedelta(minutes=1)
        for j in range(0, 10):  # we are going to send 100 request per second for 10 seconds
            begin_time_j = datetime.datetime.now()
            next_iteration_time_j = begin_time_j + datetime.timedelta(seconds=1)
            with futures3.ThreadPoolExecutor(max_workers=request_count_per_second) as pool:
                responses = list(pool.map(do_post_to_analyzer_endpoint, [url] * request_count_per_second))
                all_responses = all_responses + responses
                end_time_j = datetime.datetime.now()
            if end_time_j < next_iteration_time_j:
                remaining_sleep_time_j = (next_iteration_time_j - end_time_j).total_seconds()
                time.sleep(remaining_sleep_time_j)
        end_time_i = datetime.datetime.now()
        if end_time_i < next_iteration_time_i and i < iteration_count - 1:
            remaining_sleep_time_i = (next_iteration_time_i - end_time_i).total_seconds()
            time.sleep(remaining_sleep_time_i)
    delays = list(map(lambda response: response.elapsed.total_seconds() * 1000, all_responses))
    assert np.mean(delays) <= max_response_time_threshold