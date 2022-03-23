from flask import Flask, Response
from flask_cors import CORS

from routes.analyzer_route import app_analyzer
from routes.index_route import app_index
from services import constants_service as ct

# Create the Flask app
app = Flask(__name__)

# Add CORS handling
cors = CORS(app)

# Log the server's activity
app.debug = True

# Register the routes
app.register_blueprint(app_analyzer, url_prefix=f'/{ct.get_analyzer_endpoint_url_prefix()}')
app.register_blueprint(app_index, url_prefix=f'/{ct.get_index_endpoint_url_prefix()}')


@app.after_request
def set_response_headers(response: Response) -> Response:
    """
    Handle the application's CORS policy
    :param response: response returned to a client
    :return: the response with access control headers
    """
    response.headers.remove('Access-Control-Allow-Origin')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST')
    return response