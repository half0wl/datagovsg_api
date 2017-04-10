from .datagovsg import DataGovSG
from .transport import TransportAPI
from .environment import EnvironmentAPI

__name__ = 'datagovsg_api'
__version__ = '0.1.0'
__author__ = 'Ray Chen'
__author_email__ = 'ray@half0wl.com'
__url__ = 'https://github.com/half0wl/datagovsg_api'
__license__ = 'MIT'
__description__ = 'Unofficial API wrapper for developers.data.gov.sg'
__long_description__ = 'Visit https://github.com/half0wl/datagovsg_api for info.'


class AllAPI(TransportAPI, EnvironmentAPI):

    """
    This class exposes all available APIs, so a single instance can access
    both Transport and Environment APIs.

    Args:
        API_KEY (str): A valid API key obtained from developers.data.gov.sg.
    """
    def __init__(self, API_KEY):
        super().__init__(API_KEY)
