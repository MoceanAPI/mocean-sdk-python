from moceansdk.auth import AbstractAuth
from moceansdk.modules import AbstractClient, Transmitter


class NumberLookup(AbstractClient):

    def __init__(self, obj_auth: AbstractAuth, transmitter: Transmitter):
        super(NumberLookup, self).__init__(obj_auth, transmitter)
        self._required_fields = ['mocean-api-key', 'mocean-api-secret', 'mocean-to']

    def set_to(self, param):
        self._params['mocean-to'] = param
        return self

    def set_nl_url(self, param):
        self._params['mocean-nl-url'] = param
        return self

    def set_resp_format(self, param):
        self._params['mocean-resp-format'] = param
        return self

    def inquiry(self, params=None):
        if params is None:
            params = {}

        super(NumberLookup, self).create(params)
        self.create_final_params()
        self.is_required_field_set()

        response = self._transmitter.get('/nl', self._params)
        return response
