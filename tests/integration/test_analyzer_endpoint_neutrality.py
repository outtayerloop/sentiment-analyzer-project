import requests
import json
from tests import fake_constants_service as fct
import os

# Get current Flask app host
host = os.getenv('SENTIMENT_ANALYSIS_HOST')

# Get current Flask app port
port = os.getenv('FLASK_RUN_PORT')

expected_response_body = fct.get_neutrality_label()


def test_basic_neutral_sentence_without_punctuation_returns_neutrality_response_body():
    """
    Test if basic neutral input
    results in a response JSON body with the neutral sentiment label.
    """
    neutral_sentence = 'This is a book'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: neutral_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_basic_neutral_sentence_with_punctuation_emphasis_returns_neutrality_response_body():
    """
    Test if basic neutral input with an exclamation point
    results in a response JSON body with the neutral sentiment label.
    """
    neutral_sentence = 'This is a book!'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: neutral_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_basic_neutral_sentence_with_capitalization_emphasis_returns_neutrality_response_body():
    """
    Test if basic neutral input with the word with the most impact capitalized
    results in a response JSON body with the neutral sentiment label.
    """
    neutral_sentence = 'This is a BOOK'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: neutral_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_neutral_booster_words_returns_neutrality_response_body():
    """
    Test if a neutral input with neutral booster words
    results in a response JSON body with the neutral sentiment label.
    """
    neutral_sentence = 'A real book, indeed a book'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: neutral_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_neutral_booster_words_with_capitalization_emphasis_returns_neutrality_response_body():
    """
    Test if a neutral input with capitalized neutral booster words
    results in a response JSON body with the neutral sentiment label.
    """
    neutral_sentence = 'A REAL book, INDEED a book'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: neutral_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_neutral_slang_without_punctuation_emphasis_handling_returns_neutrality_response_body():
    """
    Test if a neutral input with slang
    results in a response JSON body with the neutral sentiment label.
    """
    neutral_sentence = 'Today is today afaik'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: neutral_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_neutral_slang_with_punctuation_emphasis_handling_returns_neutrality_response_body():
    """
    Test if a neutral input with slang and an exclamation point
    results in a response JSON body with the neutral sentiment label.
    """
    neutral_sentence = 'Today is today afaik!'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: neutral_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_neutral_slang_with_punctuation_and_capitalization_emphasis_handling_returns_neutrality_response_body():
    """
    Test if a neutral input with capitalized slang and an exclamation point
    results in a response JSON body with the neutral sentiment label.
    """
    neutral_sentence = 'Today is TODAY AFAIK!'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: neutral_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_neutral_sentence_with_time_notion_without_punctuation_returns_neutrality_response_body():
    """
    Test if a neutral input with time influence marker
    results in a response JSON body with the neutral sentiment label.
    """
    neutral_sentence = 'Sentiment analysis has been developped for some years'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: neutral_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_neutral_sentence_with_time_notion_with_punctuation_emphasis_returns_neutrality_response_body():
    """
    Test if a neutral input with time influence marker and an exclamation point
    results in a response JSON body with the neutral sentiment label.
    """
    neutral_sentence = 'Sentiment analysis has been developped for some years!'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: neutral_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_neutral_sentence_with_time_notion_with_capitalization_emphasis_returns_neutrality_response_body():
    """
    Test if a neutral input with capitalized time influence marker
    results in a response JSON body with the neutral sentiment label.
    """
    neutral_sentence = 'Sentiment analysis has been developped FOR SOME YEARS!'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: neutral_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_qualified_neutral_sentence_without_punctuation_returns_neutrality_response_body():
    """
    Test if a qualified neutral input
    results in a response JSON body with the neutral sentiment label.
    """
    neutral_sentence = 'The book was neither a chair, neither a table'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: neutral_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_qualified_neutral_sentence_with_punctuation_emphasis_returns_neutrality_response_body():
    """
    Test if a qualified neutral input and an exclamation point
    results in a response JSON body with the neutral sentiment label.
    """
    neutral_sentence = 'The book was neither a chair, neither a table!'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: neutral_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_qualified_neutral_sentence_with_capitalization_emphasis_returns_neutrality_response_body():
    """
    Test if a capitalized qualified neutral input with
    results in a response JSON body with the neutral sentiment label.
    """
    neutral_sentence = 'The book was NEITHER a chair, NEITHER a table'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: neutral_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_neutral_mixed_negation_sentence_returns_neutrality_response_body():
    """
    Test if a mixed neutral negation input
    results in a response JSON body with the neutral sentiment label.
    """
    neutral_sentence = 'The plot was a plot, but the characters are fictive and the dialog is a written script'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: neutral_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_neutral_emoticons_returns_neutrality_response_body():
    """
    Test if the use of neutral emoticons
    results in a response JSON body with the neutral sentiment label.
    """
    neutral_sentence = '\'-\' and :x'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: neutral_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_positivity_negativity_cancel_each_other_returns_neutrality_response_body():
    """
    Test if the use of negative and positive emoticons
    results in a response JSON body with the neutral sentiment label.
    """
    neutral_sentence = 'Hello :( :)'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: neutral_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_empty_sentence_returns_neutrality_response_body():
    """
    Test if an empty input
    results in a response JSON body with the neutral sentiment label.
    """
    neutral_sentence = ''
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: neutral_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body