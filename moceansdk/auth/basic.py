from moceansdk.auth import AbstractAuth


class Basic(AbstractAuth):
    def __init__(self, api_key=None, api_secret=None, api_token=""):
        self._api_key = api_key
        self._api_secret = api_secret
        self._api_token = api_token


    def set_api_key(self, value):
        self._api_key = value

    def set_api_secret(self, value):
        self._api_secret = value

    def set_api_token(self, value):
        self._api_token = value

    def get_auth_method(self):
        return "basic"

    def get_params(self):
        return {
            "mocean-api-key": self._api_key,
            "mocean-api-secret": self._api_secret,
            "mocean-api-token": self._api_token
        }
