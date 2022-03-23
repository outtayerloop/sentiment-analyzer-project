def get_positivity_label() -> str:
    """
    Return the label corresponding to a positive sentiment.
    :return: a string containing the word "positive"
    """
    return 'Positive'


def get_neutrality_label() -> str:
    """
    Return the label corresponding to a neutral sentiment.
    :return: a string containing the word "neutral"
    """
    return 'Neutral'


def get_negativity_label() -> str:
    """
    Return the label corresponding to a negative sentiment.
    :return: a string containing the word "negative"
    """
    return 'Negative'


def get_threshold() -> float:
    """
    Return the float threshold value for a sentiment compound to be interpreted positive, neutral or negative.
    :return: a float containing the value 0.05
    """
    return 0.05


def get_max_input_length() -> int:
    """
    Return the max accepted length for sentences to be analyzed by the endpoint.
    :return: an int containing the value 500
    """
    return 500


def get_analyzer_endpoint_url_prefix() -> str:
    """
    Return the analyzer endpoint url prefix
    :return: the analyzer endpoint url prefix
    """
    return 'analyzer'


def get_index_endpoint_url_prefix() -> str:
    """
    Return the index endpoint url prefix
    :return: the index endpoint url prefix
    """
    return ''


def get_application_content_type() -> str:
    """
    Return the application accepted content type
    :return: the application accepted content type
    """
    return 'application/json'


def get_analyzer_endpoint_key() -> str:
    """
    Return the accepted input key of the analyzer endpoint
    :return: the accepted input key of the analyzer endpoint
    """
    return 'input'


def get_response_message_key() -> str:
    """
    Return the response message key when the response has content
    :return: the response message key
    """
    return 'message'


def get_none_json_request_body_message() -> str:
    """
    Return the message associated with a missing content type headers 400 Bad Request response
    or None request body JSON.
    :return: the above described message
    """
    return 'Missing application/json content type in request headers or None request body JSON'


def get_missing_input_key_message() -> str:
    """
    Return the message associated with a missing input key 400 Bad Request response
    :return: the above described message
    """
    input_key = get_analyzer_endpoint_key()
    return f'POST request JSON body key "{input_key}" not found'


def get_none_input_key_message() -> str:
    """
    Return the message associated with a None input key 400 Bad Request response
    :return: the above described message
    """
    input_key = get_analyzer_endpoint_key()
    return f'POST request JSON body "{input_key}" value is null'


def get_too_big_input_length_message() -> str:
    """
    Return the message associated with a too big input length 400 Bad Request response
    :return: the above described message
    """
    max_input_length = str(get_max_input_length())
    return f'Input text too big (max {max_input_length} characters)'


def get_index_content_type() -> str:
    """
    Return the index endpoint response content type
    :return: the index endpoint response content type
    """
    return 'text/html; charset=utf-8'