import sys
import uuid

from logging import getLogger
from datetime import date, datetime
from src.location.location import Location
from src.location.geo import Geo

logger = getLogger(__name__)

class LocationService:
    def __init__(self):
        pass

    def saveLocation(self, location):
        try:
            location = Location()

            location.set_id(str(uuid.uuid4()))

            return location
        except Exception as e:
            exc_info = sys.exc_info()

            logger.error('Error on SaveLocation service', exc_info=exc_info)

            raise e

    def getLocation(self, params):
        try:
            logger.info('Searching for Location', args=params)

            location = Location()

            location.set_id(str(uuid.uuid4()))

            return location
        except Exception as e:
            exc_info = sys.exc_info()

            logger.error('Error on GetLocation service', exc_info=exc_info)

            raise e

    def updateLocation(self, location):
        try:
            location = Location()

            location.set_id(str(uuid.uuid4()))

            return location
        except Exception as e:
            exc_info = sys.exc_info()

            logger.error('Error on SaveLocation service', exc_info=exc_info)

            raise e

    def getLocationDto(self, entity):
        locationItem = Location()

        if entity.key is not None and entity.key.id is not None:
            locationItem.id = entity.key.id

        if 'geo' in entity:
            locationItem.geo = entity['geo']

            locationItem.address = self.look_up_address_for(locationItem.geo)

        if 'preciseness' in entity:
            locationItem.preciseness = entity['preciseness']

        if 'dateCreated' in entity:
            locationItem.dateCreated = entity['dateCreated'].timestamp()

        if 'dateModified' in entity:
            locationItem.dateModified = entity['dateModified'].timestamp()

        return locationItem
    
    def look_up_address_for(self, geo):
        return ''
