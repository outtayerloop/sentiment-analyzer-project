from flask import Blueprint, request, make_response, jsonify, Response
from services import extractor_service as ex
from services import constants_service as ct

# Create the analyzer route
app_analyzer = Blueprint('analyzer', __name__)


@app_analyzer.route('', methods=['POST'])
def analyze() -> Response:
    """
    Return a 200 OK Flask Response containing the extracted sentiment string
    from the request JSON "input" component if the input is valid,
    otherwise return a 400 Bad Request.
    :return: the extracted sentiment (between "positive", "neutral" and "negative"
    """
    if is_invalid_request_json(request.json):
        return get_400_response_from_input(request.json)
    user_input = request.json[ct.get_analyzer_endpoint_key()]
    extracted_sentiment = ex.get_sentiment(user_input)
    return make_response(jsonify(extracted_sentiment))


def get_400_response_from_input(request_json: dict[str, str]) -> Response:
    """
    Return a 400 Bad Request response with no content
    :return: the built Flask Response object with status code 400
    """
    response_content = get_response_400_data_by_reason(request_json)
    response = make_response(jsonify(response_content))
    response.status_code = 400
    return response


def is_invalid_request_json(request_json: dict[str, str]) -> bool:
    """
    Return whether the provided json input is None
    or has no "input" key
    or has an "input" value that has a length that is superior to the max accepted length.
    :param request_json: the user input provided from the JSON request object
    :return: True if the input is invalid, else False
    """
    input_key = ct.get_analyzer_endpoint_key()
    return request_json is None \
           or input_key not in request_json \
           or request_json[input_key] is None \
           or len(request_json[input_key]) > ct.get_max_input_length()


def get_response_400_data_by_reason(request_json: dict[str, str]) -> dict[str, str]:
    """
    Return the 400 Bad Request response data object with a different message
    for each issue.
    :param request_json: The input request JSON
    :return: the dictionary containing the relevant error message
    """
    input_key = ct.get_analyzer_endpoint_key()
    if request_json is None:
        error_message = ct.get_none_json_request_body_message()
    elif input_key not in request_json:
        error_message = ct.get_missing_input_key_message()
    elif request_json[input_key] is None:
        error_message = ct.get_none_input_key_message()
    else:
        error_message = ct.get_too_big_input_length_message()
    return {ct.get_response_message_key(): error_message}