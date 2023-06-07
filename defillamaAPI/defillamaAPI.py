import requests

BASE_URL = "https://api.llama.fi"
class Base:
    """
    """
    def __init__(self):
        """
        Initialize the object
        """
        self.session = requests.Session()

    def _send_request(self, method, endpoint, base_url=BASE_URL, params=None, data=None):
        """
        """
        url = base_url + endpoint
        response = self.session.request(method, url, params=params,
                                 data=data, timeout=60)
        return response.json()