import re

from moceansdk import RequiredFieldException
from moceansdk.modules.response_factory import ResponseFactory
from moceansdk.modules.transmitter import Transmitter


class AbstractClient(object):

    def __init__(self, obj_auth, transmitter):
        self._params = obj_auth.get_params()
        self._transmitter = transmitter
        self._required_fields = []

    def create(self, params):
        if isinstance(params, dict):
            self._params.update(dict(params))
        return self

    def create_final_params(self):
        tmp_params = dict()
        regex = re.compile('^mocean-', re.MULTILINE)
        for k, v in self._params.items():
            if v is not None:
                new_key = k
                if regex.match(k) is None:
                    new_key = "mocean-" + k
                tmp_params[new_key] = v
        self._params = tmp_params

    def is_required_field_set(self):
        for x in self._required_fields:
            if x not in self._params:
                raise RequiredFieldException("%s is mandatory field" % x)
                
    def is_api_credentials_set(self):
        if self._params['mocean-api-token'] == "":
            has_api_key = 'mocean-api-key' in self._params
            has_api_secret = 'mocean-api-secret' in self._params

            if not has_api_key and not has_api_secret:
                raise RequiredFieldException("Missing api token")

            if not has_api_key:
                raise RequiredFieldException("Missing api key")

            if not has_api_secret:
                raise RequiredFieldException("Missing api secret")
