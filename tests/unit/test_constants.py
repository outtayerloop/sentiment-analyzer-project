from services import constants_service as ct
from tests import fake_constants_service as fct


def test_positivity_label():
    """
    Test if the label of the positive sentiment is still the expected one.
    """
    expected_positivity_label = fct.get_positivity_label()
    positivity_label = ct.get_positivity_label()
    assert positivity_label == expected_positivity_label


def test_neutrality_label():
    """
    Test if the label of the neutral sentiment is still the expected one.
    """
    expected_neutrality_label = fct.get_neutrality_label()
    neutrality_label = ct.get_neutrality_label()
    assert neutrality_label == expected_neutrality_label


def test_negativity_label():
    """
    Test if the label of the negative sentiment is still the expected one.
    """
    expected_negativity_label = fct.get_negativity_label()
    negativity_label = ct.get_negativity_label()
    assert negativity_label == expected_negativity_label


def test_treshold_value():
    """
    Test if the value of the sentiment compound threshold is still the expected one.
    """
    expected_threshold_value = fct.get_threshold()
    threshold_value = ct.get_threshold()
    assert threshold_value == expected_threshold_value


def test_treshold_value_is_positive():
    """
    Test if the value of the sentiment compound threshold is superior to 0.
    """
    threshold_value = fct.get_threshold()
    assert threshold_value > 0


def test_max_input_length_value():
    """
    Test if the value of the max input length is still the expected one.
    """
    expected_max_input_length_value = fct.get_max_input_length()
    max_input_length_value = ct.get_max_input_length()
    assert max_input_length_value == expected_max_input_length_value


def test_max_input_length_value_is_positive():
    """
    Test if the value of the max input length is superior to 0.
    """
    max_input_length_value = fct.get_max_input_length()
    assert max_input_length_value > 0


def test_analyzer_endpoint_url_prefix():
    """
    Test if the URL prefix of the analyzer endpoint is still the expected one.
    """
    expected_analyzer_endpoint_url_prefix = fct.get_analyzer_endpoint_url_prefix()
    analyzer_endpoint_url_prefix = ct.get_analyzer_endpoint_url_prefix()
    assert analyzer_endpoint_url_prefix == expected_analyzer_endpoint_url_prefix


def test_index_endpoint_url_prefix():
    """
    Test if the URL prefix of the index endpoint is still the expected one.
    """
    expected_index_endpoint_url_prefix = fct.get_index_endpoint_url_prefix()
    index_endpoint_url_prefix = ct.get_index_endpoint_url_prefix()
    assert index_endpoint_url_prefix == expected_index_endpoint_url_prefix


def test_application_content_type():
    """
    Test if the application content type is still the expected one.
    """
    expected_application_content_type = fct.get_application_content_type()
    application_content_type = ct.get_application_content_type()
    assert application_content_type == expected_application_content_type


def test_analyzer_route_input_key():
    """
    Test if the input key of the analyzer endpoint is still the expected one.
    """
    expected_analyzer_endpoint_key = fct.get_analyzer_endpoint_key()
    analyzer_endpoint_key = ct.get_analyzer_endpoint_key()
    assert analyzer_endpoint_key == expected_analyzer_endpoint_key


def test_response_message_key():
    """
    Test if the response message key is still the expected one.
    """
    expected_response_message_key = fct.get_response_message_key()
    response_message_key = ct.get_response_message_key()
    assert response_message_key == expected_response_message_key


def test_none_request_body_json_message():
    """
    Test if the message associated with a missing content type headers
    or None request JSON body 400 Bad Request response
    is still the expected one.
    """
    expected_none_request_body_json_message = fct.get_none_json_request_body_message()
    none_request_body_json_message = ct.get_none_json_request_body_message()
    assert none_request_body_json_message == expected_none_request_body_json_message


def test_missing_input_key_message():
    """
    Test if the message associated with a missing input key 400 Bad Request response
    is still the expected one
    """
    expected_missing_input_key_message = fct.get_missing_input_key_message()
    missing_input_key_message = ct.get_missing_input_key_message()
    assert missing_input_key_message == expected_missing_input_key_message


def test_none_input_key_message():
    """
    Test if the message associated with a None input key 400 Bad Request response
    is still the expected one.
    """
    expected_none_input_key_message = fct.get_none_input_key_message()
    none_input_key_message = ct.get_none_input_key_message()
    assert none_input_key_message == expected_none_input_key_message


def test_too_big_input_length_message():
    """
    Test if the message associated with a too big input length 400 Bad Request response
    is still the expected one
    """
    expected_too_big_input_length_message = fct.get_too_big_input_length_message()
    too_big_input_length_message = ct.get_too_big_input_length_message()
    assert too_big_input_length_message == expected_too_big_input_length_message


def test_index_content_type():
    """
    Test if the index endpoint response content type
    is still the expected one
    """
    expected_index_content_type = fct.get_index_content_type()
    index_content_type = ct.get_index_content_type()
    assert index_content_type == expected_index_content_type