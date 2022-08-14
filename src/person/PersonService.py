import sys
import uuid
import logging
import requests

from src.person.Person import Person

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class PersonService:
    def __init__(self, healthCareRepository):
        self.__healthcareRepository = healthCareRepository

    def getPerson(self, data):
        try:
            logger.info(msg='Searching for Person')

            datasets = self.__healthcareRepository.getDataset()

            logger.info(f'No. of datasets is {datasets.length()}')

            return self.__personDto(data)
        except Exception as e:
            exc_info = sys.exc_info()

            logger.error('Error on GetLocation service', exc_info=exc_info)

            raise e

    def __personDto(self, data):
        person = Person()

        person.set_first_name(data.get('firstName', ''))
        person.set_last_name(data.get('lastName', ''))
        person.set_target(data.get('target', ''))
        person.set_id(data.get('id', ''))

        return person