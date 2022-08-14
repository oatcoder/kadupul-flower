import unittest
import os

from src.gcp.HealthcareRepository import HealthcareRepository

class HealthcareRepositoryTestCases(unittest.TestCase):
    def test_get_gcp_config(self):
        repository = HealthcareRepository()

        os.environ['GCP_ZONE'] = 'mockzone'
        os.environ['GCP_PROJECT_ID'] = 'mockprojectid'

        self.assertEquals(repository.get_gcp_config().get_project_id(), 'mockprojectid')
        self.assertEquals(repository.get_gcp_config().get_zone(), 'mockzone')