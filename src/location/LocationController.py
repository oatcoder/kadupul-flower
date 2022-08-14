import sys
import json

from flask import Flask, request, abort, Response, Blueprint
from src.location.LocationService import LocationService

location_routes = Blueprint('location_routes', __name__)

class LocationController:
    def __init__(self):
        pass

    @location_routes.route('/location/new', methods=['POST'])
    def post_location(self = {}):
        if not request.json:
            abort(400)

        location = LocationService().saveLocation(request.json)

        return Response(json.dumps(location, default=lambda x: x.__dict__), status=200, mimetype="application/json")


    @location_routes.route('/location/search', methods=['POST'])
    def get_location(self = {}):
        params = { id: request.json.get('id', '')}

        location = LocationService().getLocation(params)

        return Response(json.dumps(location, default=lambda x: x.__dict__), status=200, mimetype="application/json")


    @location_routes.route('/location/update', methods=['POST'])
    def put_location(self = {}):
        if not request.json:
            abort(400)

        location = LocationService().updateLocation(id, request.get_json())

        return Response(json.dumps(location, default=lambda x: x.__dict__), status=200, mimetype="application/json")