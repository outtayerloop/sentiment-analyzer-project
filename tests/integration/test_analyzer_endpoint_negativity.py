import requests
import json
from tests import fake_constants_service as fct
import os

# Get current Flask app host
host = os.getenv('SENTIMENT_ANALYSIS_HOST')

# Get current Flask app port
port = os.getenv('FLASK_RUN_PORT')

expected_response_body = fct.get_negativity_label()


def test_basic_negative_sentence_without_punctuation_returns_negativity_response_body():
    """
    Test if basic negative input
    results in a response JSON body with the negative sentiment label.
    """
    negative_sentence = 'This is a terrible book'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: negative_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_basic_negative_sentence_with_punctuation_emphasis_returns_negativity_response_body():
    """
    Test if basic negative input with an exclamation point
    results in a response JSON body with the negative sentiment label.
    """
    negative_sentence = 'This is a terrible book!'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: negative_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_basic_negative_sentence_with_capitalization_emphasis_returns_negativity_response_body():
    """
    Test if basic negative input with the word with the most impact capitalized
    results in a response JSON body with the negative sentiment label.
    """
    negative_sentence = 'This is a TERRIBLE book'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: negative_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_negative_booster_words_returns_negativity_response_body():
    """
    Test if a negative input with negative booster words
    results in a response JSON body with the negative sentiment label.
    """
    negative_sentence = 'A really bad, horrible book'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: negative_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_negative_booster_words_with_capitalization_emphasis_returns_negativity_response_body():
    """
    Test if a negative input with capitalized negative booster words
    results in a response JSON body with the negative sentiment label.
    """
    negative_sentence = 'A REALLY bad, HORRIBLE book'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: negative_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_negative_slang_without_punctuation_emphasis_handling_returns_negativity_response_body():
    """
    Test if a negative input with slang
    results in a response JSON body with the negative sentiment label.
    """
    negative_sentence = 'Today sux'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: negative_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_negative_slang_with_punctuation_emphasis_handling_returns_negativity_response_body():
    """
    Test if a negative input with slang and an exclamation point
    results in a response JSON body with the negative sentiment label.
    """
    negative_sentence = 'Today sux!'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: negative_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_negative_slang_with_punctuation_and_capitalization_emphasis_handling_returns_negativity_response_body():
    """
    Test if a negative input with capitalized slang and an exclamation point
    results in a response JSON body with the negative sentiment label.
    """
    negative_sentence = 'Today SUX!'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: negative_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_negative_insult_without_punctuation_returns_negativity_response_body():
    """
    Test if a negative input with an insult
    results in a response JSON body with the negative sentiment label.
    """
    negative_sentence = 'Most automated sentiment analysis tools are shit'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: negative_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_negative_insult_with_punctuation_emphasis_returns_negativity_response_body():
    """
    Test if a negative input with an insult and an exclamation point
    results in a response JSON body with the negative sentiment label.
    """
    negative_sentence = 'Most automated sentiment analysis tools are shit!'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: negative_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_negative_insult_with_capitalization_emphasis_returns_negativity_response_body():
    """
    Test if a negative input with a capitalzed insult and an exclamation point
    results in a response JSON body with the negative sentiment label.
    """
    negative_sentence = 'Most automated sentiment analysis tools are SHIT'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: negative_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_negative_sentence_with_time_notion_without_punctuation_returns_negativity_response_body():
    """
    Test if a negative input with time influence marker
    results in a response JSON body with the negative sentiment label.
    """
    negative_sentence = 'Sentiment analysis has never been good'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: negative_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_negative_sentence_with_time_notion_with_punctuation_emphasis_returns_negativity_response_body():
    """
    Test if a negative input with time influence marker and an exclamation point
    results in a response JSON body with the negative sentiment label.
    """
    negative_sentence = 'Sentiment analysis has never been good!'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: negative_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_negative_sentence_with_time_notion_with_capitalization_emphasis_returns_negativity_response_body():
    """
    Test if a negative input with capitalized time influence marker
    results in a response JSON body with the negative sentiment label.
    """
    negative_sentence = 'Sentiment analysis has NEVER BEEN GOOD!'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: negative_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_qualified_negative_sentence_without_punctuation_returns_negativity_response_body():
    """
    Test if a qualified negative input
    results in a response JSON body with the negative sentiment label.
    """
    negative_sentence = 'The book was kind of bad'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: negative_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_qualified_negative_sentence_with_punctuation_emphasis_returns_negativity_response_body():
    """
    Test if a qualified negative input and an exclamation point
    results in a response JSON body with the negative sentiment label.
    """
    negative_sentence = 'The book was kind of bad!'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: negative_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_qualified_negative_sentence_with_capitalization_emphasis_returns_negativity_response_body():
    """
    Test if a capitalized qualified negative input with
    results in a response JSON body with the negative sentiment label.
    """
    negative_sentence = 'The book was KIND OF bad'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: negative_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_negative_mixed_negation_sentence_returns_negativity_response_body():
    """
    Test if a mixed negative negation input
    results in a response JSON body with the negative sentiment label.
    """
    negative_sentence = 'The plot was good, but the characters are uncompelling and the dialog is not great'
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: negative_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body


def test_negative_emoticons_returns_negativity_response_body():
    """
    Test if the use of negative emoticons
    results in a response JSON body with the negative sentiment label.
    """
    negative_sentence = ':( and :\'('
    url_prefix = fct.get_analyzer_endpoint_url_prefix()
    url = f'http://{host}:{port}/{url_prefix}'
    input_key = fct.get_analyzer_endpoint_key()
    valid_input = json.dumps({input_key: negative_sentence})
    content_type = fct.get_application_content_type()
    headers = {'content-type': content_type}
    response = requests.post(url, data=valid_input, headers=headers)
    body = json.loads(response.content.decode('utf-8'))
    assert body == expected_response_body