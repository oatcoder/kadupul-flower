import logging
import json

from flask import Flask
from flask_cors import CORS, cross_origin
from src.location.LocationController import location_routes
from src.person.PersonController import person_routes

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

app = Flask(__name__)
CORS(app)

app.register_blueprint(person_routes)
app.register_blueprint(location_routes)

@app.errorhandler(500)
def server_error(e):
    logger.exception('error during request')
    return """
    Internal error occurred: <pre>{}</pre>
    See logs.
    """.format(e), 500

@app.errorhandler(400)
def bad_request(e):
    logger.exception('error during request')
    return """
    Bad Request: <pre>{}</pre>
    See logs.
    """.format(e), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
