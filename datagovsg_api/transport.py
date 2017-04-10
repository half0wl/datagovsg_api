from .datagovsg import DataGovSG


class TransportAPI(DataGovSG):

    """
    https://developers.data.gov.sg/transport/

    This class contains APIs under the Transport category.

    Args:
        API_KEY (str): A valid API key obtained from developers.data.gov.sg.
    """

    def __init__(self, API_KEY):
        super(TransportAPI, self).__init__(API_KEY)

    def taxi_availability(self, date_time=None):
        """
        https://developers.data.gov.sg/transport/taxi-availability

        List of all available taxis, retrieved every 30 seconds from LTA's
        Datamall.

        Args:
            date_time (str, optional): Latest available data at that moment in
                time. Use the format ``YYYY-MM-DD[T]HH:mm:ss (SGT)``,
                for example: ``2016-12-12T09:45:00``.

        Returns:
            A ``Response`` object. Call ``.json()`` to get the json data.
            The returned json of this method is valid GeoJSON.
        """
        params = {}
        if date_time:
            params['date_time'] = date_time
        return self.get('transport/taxi-availability', params)

    def traffic_images(self, date_time=None):
        """
        https://developers.data.gov.sg/transport/traffic-images

        Images from traffic cams with camera location. Retrieved every 20
        seconds from LTA's Datamall.

        Args:
            date_time (str, optional): Latest available data at that moment in
                time. Use the format ``YYYY-MM-DD[T]HH:mm:ss (SGT)``,
                for example: ``2016-12-12T09:45:00``.

        Returns:
            A ``Response`` object. Call ``.json()`` to get the json data.
        """
        params = {}
        if date_time:
            params['date_time'] = date_time
        return self.get('transport/traffic-images', params)
