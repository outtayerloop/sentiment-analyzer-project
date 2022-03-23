from routes import analyzer_route as ar
from tests import fake_constants_service as fct


def test_none_request_json_returns_true():
    """
    Test if the bool value returned by the corresponding method of the analyzer route
    is True when the provided input is None.
    """
    invalid_request_json = None
    is_invalid_request_json = ar.is_invalid_request_json(invalid_request_json)
    assert is_invalid_request_json


def test_no_request_json_input_key_returns_true():
    """
    Test if the bool value returned by the corresponding method of the analyzer route
    is True when the provided input is None.
    """
    invalid_request_json = {}
    is_invalid_request_json = ar.is_invalid_request_json(invalid_request_json)
    assert is_invalid_request_json


def test_none_request_json_input_value_returns_true():
    """
    Test if the bool value returned by the corresponding method of the analyzer route
    is True when the provided input is None.
    """
    input_key = fct.get_analyzer_endpoint_key()
    invalid_request_json = {input_key: None}
    is_invalid_request_json = ar.is_invalid_request_json(invalid_request_json)
    assert is_invalid_request_json


def test_too_big_input_returns_true():
    """
    Test if the bool value returned by the corresponding method of the analyzer route
    is True when the provided input is too big.
    """
    input_key = fct.get_analyzer_endpoint_key()
    invalid_request_json = {input_key: 'x' * (fct.get_max_input_length() + 1)}
    is_invalid_request_json = ar.is_invalid_request_json(invalid_request_json)
    assert is_invalid_request_json


def test_valid_input_returns_false():
    """
    Test if the bool value returned by the corresponding method of the analyzer route
    is False when the provided input is not None and respects the max length value.
    """
    input_key = fct.get_analyzer_endpoint_key()
    valid_request_json = {input_key: 'x' * fct.get_max_input_length()}
    is_invalid_input = ar.is_invalid_request_json(valid_request_json)
    assert not is_invalid_input


def test_none_request_json_returns_none_request_json_message():
    """
    Test if the message associated with missing headers or None request body JSON is the expected one.
    """
    invalid_request_json = None
    response_data = ar.get_response_400_data_by_reason(invalid_request_json)
    response_message_key = fct.get_response_message_key()
    assert response_message_key in response_data
    assert response_data[response_message_key] == fct.get_none_json_request_body_message()


def test_none_request_json_input_key_returns_missing_input_key_message():
    """
    Test if the message associated with missing input key is the expected one.
    """
    invalid_request_json = {}
    response_data = ar.get_response_400_data_by_reason(invalid_request_json)
    response_message_key = fct.get_response_message_key()
    assert response_message_key in response_data
    assert response_data[response_message_key] == fct.get_missing_input_key_message()


def test_none_request_json_input_value_returns_missing_input_value_message():
    """
    Test if the message associated with None input key is the expected one.
    """
    input_key = fct.get_analyzer_endpoint_key()
    invalid_request_json = {input_key: None}
    response_data = ar.get_response_400_data_by_reason(invalid_request_json)
    response_message_key = fct.get_response_message_key()
    assert response_message_key in response_data
    assert response_data[response_message_key] == fct.get_none_input_key_message()


def test_too_big_input_length_returns_too_big_input_length_message():
    """
    Test if the message associated with a too big input length is the expected one.
    """
    input_key = fct.get_analyzer_endpoint_key()
    invalid_request_json = {input_key: 'x' * (fct.get_max_input_length() + 1)}
    response_data = ar.get_response_400_data_by_reason(invalid_request_json)
    response_message_key = fct.get_response_message_key()
    assert response_message_key in response_data
    assert response_data[response_message_key] == fct.get_too_big_input_length_message()