import os
import unittest

from datagovsg import DataGovSG


class TestDataGovSG(unittest.TestCase):

    def setUp(self):
        self.client = DataGovSG(API_KEY=os.environ['DataGovSG_APIKEY'])

    def test_build_url(self):
        expected = 'https://api.data.gov.sg/v1/environment/psi'
        built = self.client.build_url('environment/psi')

        self.assertEqual(built, expected)

    def test_get(self):
        resp = self.client.get('environment/psi', params=None)
        self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()
