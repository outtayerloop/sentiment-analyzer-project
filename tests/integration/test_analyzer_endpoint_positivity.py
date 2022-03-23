import requests
import json
from tests import fake_constants_service as fct
import os

# Get current Flask app host
host = os.getenv('SENTIMENT_ANALYSIS_HOST')

# Get current Flask app port
port = os.getenv('FLASK_RUN_PORT')

expected_response_body = fct.get_positivity_label()


def test_basic_positive_sentence_without_punctuation_returns_positivity_response_body():
    """
    Test if basic positive input
    results in a response JSON body with the positive sentiment label.
    """
    positive_sentence = 'This is a wonderful book'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: positive_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_basic_positive_sentence_with_punctuation_emphasis_returns_positivity_response_body():
    """
    Test if basic positive input with an exclamation point
    results in a response JSON body with the positive sentiment label.
    """
    positive_sentence = 'This is a wonderful book!'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: positive_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_basic_positive_sentence_with_capitalization_emphasis_returns_positivity_response_body():
    """
    Test if basic positive input with the word with the most impact capitalized
    results in a response JSON body with the positive sentiment label.
    """
    positive_sentence = 'This is a WONDERFUL book'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: positive_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_positive_booster_words_returns_positivity_response_body():
    """
    Test if a positive input with positive booster words
    results in a response JSON body with the positive sentiment label.
    """
    positive_sentence = 'A really good, great book'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: positive_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_positive_booster_words_with_capitalization_emphasis_returns_positivity_response_body():
    """
    Test if a positive input with capitalized positive booster words
    results in a response JSON body with the positive sentiment label.
    """
    positive_sentence = 'A REALLY good, GREAT book'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: positive_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_positive_slang_without_punctuation_emphasis_handling_returns_positivity_response_body():
    """
    Test if a positive input with slang
    results in a response JSON body with the positive sentiment label.
    """
    positive_sentence = 'Today is gr8'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: positive_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_positive_slang_with_punctuation_emphasis_handling_returns_positivity_response_body():
    """
    Test if a positive input with slang and an exclamation point
    results in a response JSON body with the positive sentiment label.
    """
    positive_sentence = 'Today is gr8!'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: positive_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_positive_slang_with_punctuation_and_capitalization_emphasis_handling_returns_positivity_response_body():
    """
    Test if a positive input with capitalized slang and an exclamation point
    results in a response JSON body with the positive sentiment label.
    """
    positive_sentence = 'Today is GR8!'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: positive_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_positive_sentence_with_time_notion_without_punctuation_returns_positivity_response_body():
    """
    Test if a positive input with time influence marker
    results in a response JSON body with the positive sentiment label.
    """
    positive_sentence = 'Sentiment analysis has always been good'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: positive_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_positive_sentence_with_time_notion_with_punctuation_emphasis_returns_positivity_response_body():
    """
    Test if a positive input with time influence marker and an exclamation point
    results in a response JSON body with the positive sentiment label.
    """
    positive_sentence = 'Sentiment analysis has always been good!'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: positive_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_positive_sentence_with_time_notion_with_capitalization_emphasis_returns_positivity_response_body():
    """
    Test if a positive input with capitalized time influence marker
    results in a response JSON body with the positive sentiment label.
    """
    positive_sentence = 'Sentiment analysis has ALWAYS BEEN GOOD!'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: positive_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_qualified_positive_sentence_without_punctuation_returns_positivity_response_body():
    """
    Test if a qualified positive input
    results in a response JSON body with the positive sentiment label.
    """
    positive_sentence = 'The book was kind of good'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: positive_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_qualified_positive_sentence_with_punctuation_emphasis_returns_positivity_response_body():
    """
    Test if a qualified positive input and an exclamation point
    results in a response JSON body with the positive sentiment label.
    """
    positive_sentence = 'The book was kind of good!'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: positive_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_qualified_positive_sentence_with_capitalization_emphasis_returns_positivity_response_body():
    """
    Test if a capitalized qualified positive input with
    results in a response JSON body with the positive sentiment label.
    """
    positive_sentence = 'The book was KIND OF good'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: positive_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_positive_mixed_negation_sentence_returns_positivity_response_body():
    """
    Test if a mixed positive negation input
    results in a response JSON body with the positive sentiment label.
    """
    positive_sentence = 'The plot was boring, but the characters are great and the dialog is not bad'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: positive_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_positive_emoticons_returns_positivity_response_body():
    """
    Test if the use of positive emoticons
    results in a response JSON body with the positive sentiment label.
    """
    positive_sentence = ':) and :D'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: positive_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body