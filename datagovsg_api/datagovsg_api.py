import requests


class APIClient(object):

    """
    Unofficial API Wrapper for public APIs at developers.data.gov.sg.

    Args:
        API_KEY (str): A valid API key obtained from developers.data.gov.sg.
    """

    def __init__(self, API_KEY):
        self._base_endpoint_url = 'https://api.data.gov.sg/v1'
        self.API_KEY = API_KEY

    def _build_request_url(self, endpoint):
        """
        Build the request url.

        Args:
            endpoint (str): Endpoint of the request (e.g. 'environment/psi').

        Returns:
            str: The built/final URL to the endpoint.
        """
        return '{}/{}'.format(self._base_endpoint_url, endpoint)

    def _make_request(self, endpoint, params):
        """
        Base method for making requests to the API endpoint.

        Args:
            endpoint (str): Endpoint of the request (e.g. 'environment/psi').
            params (dict, optional): Request parameters.

        Returns:
            A ``Response`` object.
        """
        request_headers = {'api-key': self.API_KEY}
        endpoint_url = self._build_request_url(endpoint)
        return requests.get(endpoint_url,
                            headers=request_headers,
                            params=params)

    # --------------------------------
    # Category: Transport
    # --------------------------------

    def taxi_availability(self, date_time=None):
        """
        https://developers.data.gov.sg/transport/taxi-availability

        List of all available taxis, retrieved every 30 seconds from LTA's
        Datamall.

        Args:
            date_time (str, optional): Latest available data at that
                moment in time. Use the format ``YYYY-MM-DD[T]HH:mm:ss (SGT)``
                , for example: ``2016-12-12T09:45:00``.

        Returns:
            A ``Response`` object. Call ``.json()`` to get the json (dict)
            representation of the data. E.g. ``taxi_availability().json()``.
            The json is a valid GeoJSON.
        """
        endpoint = 'transport/taxi-availability'
        params = {}
        if date_time:
            params['date_time'] = date_time
        return self._make_request(endpoint, params)

    def traffic_images(self, date_time=None):
        """
        https://developers.data.gov.sg/transport/traffic-images

        Images from traffic cams with camera location. Retrieved every 20
        seconds from LTA's Datamall.

        Args:
            date_time (str, optional): Latest available data at that
                moment in time. Use the format ``YYYY-MM-DD[T]HH:mm:ss (SGT)``
                , for example: ``2016-12-12T09:45:00``.

        Returns:
            A ``Response`` object. Call ``.json()`` to get the json (dict)
            representation of the data. E.g. ``traffic_images().json()``.
        """
        endpoint = 'transport/traffic-images'
        params = {}
        if date_time:
            params['date_time'] = date_time
        return self._make_request(endpoint, params)

    # --------------------------------
    # Category: Environment
    # --------------------------------

    def weather_forecast(self, duration, date=None, date_time=None):
        """
        https://developers.data.gov.sg/environment/2-hour-weather-forecast
        https://developers.data.gov.sg/environment/24-hour-weather-forecast
        https://developers.data.gov.sg/environment/4-day-weather-forecast

        Weather forecast. 2-hour forecast is retrieved half-hourly from NEA,
        24-hour is retrieved multiple times throughout the day, and 4-day is
        retrieved twice a day from NEA.

        Args:
            duration (str): The duration to retrieve, i.e.: ``'2-hour'``,
                ``'24-hour'``, ``'4-day'``.
            date (str, optional): All of the forecasts issued for that day.
                Use the format ``YYYY-MM-DD``, for example: ``2016-12-12``.
            date_time (str, optional): Latest forecast issued at that moment
                in time. Use the format ``YYYY-MM-DD[T]HH:mm:ss (SGT)``
                , for example: ``2016-12-12T09:45:00``.

        Returns:
            A ``Response`` object. Call ``.json()`` to get the json (dict)
            representation of the data.
            E.g. ``weather_forecast(duration='4-day').json()``.

        Raises:
            Exception: Duration must be a string '2-hour', '24-hour', '4-day'.
        """
        if duration == '2-hour':
            endpoint = 'environment/2-hour-weather-forecast'
        elif duration == '24-hour':
            endpoint = 'environment/24-hour-weather-forecast'
        elif duration == '4-day':
            endpoint = 'environment/4-day-weather-forecast'
        else:
            raise Exception(
                'Duration must be a string \
                (\'2-hour\', \'24-hour\', \'4-day\')'
            )

        params = {}
        if date:
            params['date'] = date
        if date_time:
            params['date_time'] = date_time

        return self._make_request(endpoint, params)

    def air_temperature(self):
        raise NotImplementedError

    def pm25(self):
        raise NotImplementedError

    def psi(self):
        raise NotImplementedError

    def rainfall(self):
        raise NotImplementedError

    def relative_humidity(self):
        raise NotImplementedError

    def uv_index(self):
        raise NotImplementedError

    def wind_direction(self):
        raise NotImplementedError

    def wind_speed(self):
        raise NotImplementedError
