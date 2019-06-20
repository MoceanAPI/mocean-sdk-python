from moceansdk.modules import AbstractClient


class Balance(AbstractClient):

    def __init__(self, obj_auth, transmitter):
        super(Balance, self).__init__(obj_auth, transmitter)
        self._required_fields = ['mocean-api-key', 'mocean-api-secret']

    def set_resp_format(self, param):
        self._params['mocean-resp-format'] = param
        return self

    def inquiry(self, params=None):
        if params is None:
            params = {}

        super(Balance, self).create(params)
        self.create_final_params()
        self.is_required_field_set()

        return self._transmitter.get('/account/balance', self._params)
