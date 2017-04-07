import unittest
import requests
import os

import datagovsg_api


class TestAPIClient(unittest.TestCase):

    def setUp(self):
        self.client = datagovsg_api.APIClient(
            API_KEY=os.environ['DataGovSG_APIKEY']
        )

    def test_build_request_url(self):
        expected_url = 'https://api.data.gov.sg/v1/environment/psi'
        endpoint = 'environment/psi'
        built_url = self.client._build_request_url(endpoint)
        self.assertEqual(built_url, expected_url)

    def test_can_make_request(self):
        resp = self.client._make_request('environment/psi', params=None)
        self.assertEqual(resp.status_code, 200)

    def test_taxi_availability(self):
        resp = self.client.taxi_availability()
        self.assertEqual(resp.status_code, 200)

    def test_traffic_images(self):
        resp = self.client.traffic_images()
        self.assertEqual(resp.status_code, 200)

    def test_weather_forecast(self):
        resp_2h = self.client.weather_forecast(duration='2-hour')
        resp_24h = self.client.weather_forecast(duration='24-hour')
        resp_4d = self.client.weather_forecast(duration='4-day')
        self.assertEqual(resp_2h.status_code, 200)
        self.assertEqual(resp_24h.status_code, 200)
        self.assertEqual(resp_4d.status_code, 200)
        self.assertRaises(Exception,
                          self.client.weather_forecast,
                          duration='test')

    def test_air_temperature(self):
        pass

    def test_pm25(self):
        pass

    def test_psi(self):
        pass

    def test_rainfall(self):
        pass

    def test_relative_humidity(self):
        pass

    def test_uv_index(self):
        pass

    def test_wind_direction(self):
        pass

    def test_wind_speed(self):
        pass

if __name__ == '__main__':
    unittest.main()
