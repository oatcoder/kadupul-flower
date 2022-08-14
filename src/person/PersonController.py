import sys
import json
import logging

from flask import Flask, request, abort, Response, Blueprint
from src.person.PersonService import PersonService
from src.gcp.HealthcareRepository import HealthcareRepository
from src.ErrorResponse import ErrorResponse

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

person_routes = Blueprint('person_routes', __name__)

class PersonController:
    def __init__(self):
        pass

    @person_routes.route('/person/search', methods=['POST'])
    def get_person(self = {}):
        try:
            if not request.json:
                abort(400)

            healthCareRepository = HealthcareRepository()

            person = PersonService(healthCareRepository=healthCareRepository).getPerson(request.json)

            return Response(json.dumps(person, default=lambda x: x.__dict__), status=200, mimetype="application/json")
        except Exception as e:
            errMsg = f'Person Search Controller throw an exception.'

            errResponse = ErrorResponse()

            errResponse.set_title(errMsg)
            errResponse.set_detail(e.__str__())
            errResponse.set_status(500)
            errResponse.set_source_pointer('Person Search Controller')

            logger.error(errMsg, exc_info=sys.exc_info())

            jsonErr = json.dumps(errResponse, default=lambda x: x.__dict__)

            abort(Response(jsonErr, status=500, mimetype="application/json"))