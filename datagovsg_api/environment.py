from .datagovsg import DataGovSG


class EnvironmentAPI(DataGovSG):

    """
    https://developers.data.gov.sg/environment/

    This class contains APIs under the Environment category.

    Args:
        API_KEY (str): A valid API key obtained from developers.data.gov.sg.
    """

    def __init__(self, API_KEY):
        super(EnvironmentAPI, self).__init__(API_KEY)

    def weather_forecast(self, duration, date=None, date_time=None):
        """
        https://developers.data.gov.sg/environment/2-hour-weather-forecast
        https://developers.data.gov.sg/environment/24-hour-weather-forecast
        https://developers.data.gov.sg/environment/4-day-weather-forecast

        Weather forecast. 2-hour forecast is retrieved half-hourly from NEA,
        24-hour is retrieved multiple times throughout the day, and 4-day is
        retrieved twice a day from NEA.

        Args:
            duration (str): The duration to retrieve: ``'2-hour'``,
                ``'24-hour'``, ``'4-day'``.
            date (str, optional): All data on that day. Use the format
                ``YYYY-MM-DD``, for example: ``2016-12-12``.
            date_time (str, optional): Latest available data at that moment in
                time. Use the format ``YYYY-MM-DD[T]HH:mm:ss (SGT)``,
                for example: ``2016-12-12T09:45:00``.

        Returns:
            A ``Response`` object. Call ``.json()`` to get the json data.

        Raises:
            Exception: Duration must be a string '2-hour', '24-hour', '4-day'.
        """
        params = {}
        if date:
            params['date'] = date
        if date_time:
            params['date_time'] = date_time

        if duration == '2-hour':
            return self.get('environment/2-hour-weather-forecast', params)
        elif duration == '24-hour':
            return self.get('environment/24-hour-weather-forecast', params)
        elif duration == '4-day':
            return self.get('environment/4-day-weather-forecast', params)
        else:
            raise Exception(
                'Duration must be a string (2-hour, 24-hour, 4-day)'
            )

    def air_temperature(self, date=None, date_time=None):
        """
        https://developers.data.gov.sg/environment/air-temperature

        Air temperature readings across Singapore. Per-minute readings from
        NEA.

        Args:
            date (str, optional): All data on that day. Use the format
                ``YYYY-MM-DD``, for example: ``2016-12-12``.
            date_time (str, optional): Latest available data at that moment in
                time. Use the format ``YYYY-MM-DD[T]HH:mm:ss (SGT)``,
                for example: ``2016-12-12T09:45:00``.

        Returns:
            A ``Response`` object. Call ``.json()`` to get the json data.
        """
        params = {}
        if date:
            params['date'] = date
        if date_time:
            params['date_time'] = date_time
        return self.get('environment/air-temperature', params)

    def pm25(self, date=None, date_time=None):
        """
        https://developers.data.gov.sg/environment/pm25

        PM2.5 readings across Singapore. Retrieved hourly from NEA.

        Args:
            date (str, optional): All data on that day. Use the format
                ``YYYY-MM-DD``, for example: ``2016-12-12``.
            date_time (str, optional): Latest available data at that moment in
                time. Use the format ``YYYY-MM-DD[T]HH:mm:ss (SGT)``,
                for example: ``2016-12-12T09:45:00``.

        Returns:
            A ``Response`` object. Call ``.json()`` to get the json data.
            The ``region_metadata`` field in the response contains the
            lat/lon for the regions.
        """
        params = {}
        if date:
            params['date'] = date
        if date_time:
            params['date_time'] = date_time
        return self.get('environment/air-temperature', params)

    def psi(self, date=None, date_time=None):
        """
        https://developers.data.gov.sg/environment/psi

        PSI readings across Singapore. Retrieved hourly from NEA.

        Args:
            date (str, optional): All data on that day. Use the format
                ``YYYY-MM-DD``, for example: ``2016-12-12``.
            date_time (str, optional): Latest available data at that moment in
                time. Use the format ``YYYY-MM-DD[T]HH:mm:ss (SGT)``,
                for example: ``2016-12-12T09:45:00``.

        Returns:
            A ``Response`` object. Call ``.json()`` to get the json data.
            The ``region_metadata`` field in the response contains the
            lat/lon for the regions.
        """
        params = {}
        if date:
            params['date'] = date
        if date_time:
            params['date_time'] = date_time
        return self.get('environment/psi', params)

    def rainfall(self, date=None, date_time=None):
        """
        https://developers.data.gov.sg/environment/rainfall

        Rainfall readings across Singapore. 5-minute readings from NEA.

        Args:
            date (str, optional): All data on that day. Use the format
                ``YYYY-MM-DD``, for example: ``2016-12-12``.
            date_time (str, optional): Latest available data at that moment in
                time. Use the format ``YYYY-MM-DD[T]HH:mm:ss (SGT)``,
                for example: ``2016-12-12T09:45:00``.

        Returns:
            A ``Response`` object. Call ``.json()`` to get the json data.
        """
        params = {}
        if date:
            params['date'] = date
        if date_time:
            params['date_time'] = date_time
        return self.get('environment/rainfall', params)

    def relative_humidity(self, date=None, date_time=None):
        """
        https://developers.data.gov.sg/environment/relative_humidity

        Relative humidity readings across Singapore. Per-minute readings from
        NEA.

        Args:
            date (str, optional): All data on that day. Use the format
                ``YYYY-MM-DD``, for example: ``2016-12-12``.
            date_time (str, optional): Latest available data at that moment in
                time. Use the format ``YYYY-MM-DD[T]HH:mm:ss (SGT)``,
                for example: ``2016-12-12T09:45:00``.

        Returns:
            A ``Response`` object. Call ``.json()`` to get the json data.
        """
        params = {}
        if date:
            params['date'] = date
        if date_time:
            params['date_time'] = date_time
        return self.get('environment/relative-humidity', params)

    def uv_index(self, date=None, date_time=None):
        """
        https://developers.data.gov.sg/environment/uv-index

        UV index readings across Singapore. Retrieved every hour between 7AM
        and 7PM everyday.

        Args:
            date (str, optional): All data on that day. Use the format
                ``YYYY-MM-DD``, for example: ``2016-12-12``.
            date_time (str, optional): Latest available data at that moment in
                time. Use the format ``YYYY-MM-DD[T]HH:mm:ss (SGT)``,
                for example: ``2016-12-12T09:45:00``.

        Returns:
            A ``Response`` object. Call ``.json()`` to get the json data.
        """
        params = {}
        if date:
            params['date'] = date
        if date_time:
            params['date_time'] = date_time
        return self.get('environment/uv-index', params)

    def wind_direction(self, date=None, date_time=None):
        """
        https://developers.data.gov.sg/environment/wind-direction

        Wind direction readings readings across Singapore. Per-minute readings
        from NEA.

        Args:
            date (str, optional): All data on that day. Use the format
                ``YYYY-MM-DD``, for example: ``2016-12-12``.
            date_time (str, optional): Latest available data at that moment in
                time. Use the format ``YYYY-MM-DD[T]HH:mm:ss (SGT)``,
                for example: ``2016-12-12T09:45:00``.

        Returns:
            A ``Response`` object. Call ``.json()`` to get the json data.
        """
        params = {}
        if date:
            params['date'] = date
        if date_time:
            params['date_time'] = date_time
        return self.get('environment/wind-direction', params)

    def wind_speed(self, date=None, date_time=None):
        """
        https://developers.data.gov.sg/environment/wind-speed

        Wind speed readings across Singapore. Per-minute readings from NEA.

        Args:
            date (str, optional): All data on that day. Use the format
                ``YYYY-MM-DD``, for example: ``2016-12-12``.
            date_time (str, optional): Latest available data at that moment in
                time. Use the format ``YYYY-MM-DD[T]HH:mm:ss (SGT)``,
                for example: ``2016-12-12T09:45:00``.

        Returns:
            A ``Response`` object. Call ``.json()`` to get the json data.
        """
        params = {}
        if date:
            params['date'] = date
        if date_time:
            params['date_time'] = date_time
        return self.get('environment/wind-speed', params)
