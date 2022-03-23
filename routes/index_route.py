from flask import Blueprint, render_template
from services import constants_service as ct
import os

# Create the index route
app_index = Blueprint('index', __name__)


@app_index.route('', methods=['GET'])
def index() -> str:
    """
    Return the HTML index template file to display the front-end web-page
    :return: a string containing the front-end HTML web page as well as variables in the web page
    """
    host = os.getenv('SENTIMENT_ANALYSIS_HOST')
    port = os.getenv('FLASK_RUN_PORT')
    url_prefix = ct.get_analyzer_endpoint_url_prefix()
    application_content_type = ct.get_application_content_type()
    input_key = ct.get_analyzer_endpoint_key()
    return render_template('index.html',
                           analyzerEndpointUrl=f'http://{host}:{port}/{url_prefix}',
                           applicationContentType=application_content_type,
                           inputKey=input_key)