from moceansdk.auth import AbstractAuth


class Basic(AbstractAuth):
    def __init__(self, api_key=None, api_secret=None):
        self._api_key = api_key
        self._api_secret = api_secret

    def set_api_key(self, value):
        self._api_key = value

    def set_api_secret(self, value):
        self._api_secret = value

    def get_auth_method(self):
        return "basic"

    def get_params(self):
        return {
            "mocean-api-key": self._api_key,
            "mocean-api-secret": self._api_secret
        }
