import requests


class DataGovSG():

    """
    Base class for API wrappers to inherit from.

    Args:
        API_KEY (str): A valid API key obtained from developers.data.gov.sg.
    """

    def __init__(self, API_KEY):
        self.base_endpoint = 'https://api.data.gov.sg/v1'
        self.API_KEY = API_KEY

    def build_url(self, endpoint):
        """
        Build the request url.

        Args:
            endpoint (str): Endpoint of the request (e.g. 'environment/psi').

        Returns:
            str: The built/final URL to the endpoint.
        """
        return '{}/{}'.format(self.base_endpoint, endpoint)

    def get(self, endpoint, params):
        """
        Base method for making requests to the API endpoint.

        Args:
            endpoint (str): Endpoint of the request (e.g. 'environment/psi').
            params (dict, optional): Request parameters.

        Returns:
            A ``Response`` object.
        """
        headers = {'api-key': self.API_KEY}
        endpoint = self.build_url(endpoint)
        return requests.get(endpoint, headers=headers, params=params)
