import os
import requests
import sys
import logging

from src.gcp.GcpConfig import GcpConfig

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class HealthcareRepository:
    def __init__(self):
        pass

    def getDataset(self, params = None):
        try:
            logger.info(msg='List Datasets')

            if self.get_gcp_config().get_project_id() is None:
                raise Exception('GCP Project ID env var is missing')

            if self.get_gcp_config().get_zone() is None:
                raise Exception('GCP Zone env var is missing')

            r = requests.get(f'https://healthcare.googleapis.com/v1/{self.get_gcp_config().get_project_id()}/{self.get_gcp_config().get_zone()}/datasets')

            if r.status_code == 200:
                pass
            else:
                logger.warning(msg='Dataset response was not succesful', exc_info=sys.exc_info(), extra=r)
                return []
        except Exception as e:
            logger.error('Error on Listing Datasets', exc_info=sys.exc_info())
            raise e

    def get_gcp_config(self):
        result = GcpConfig()

        result.set_project_id(os.getenv('GCP_PROJECT_ID'))
        result.set_zone(os.getenv('GCP_ZONE'))

        return result