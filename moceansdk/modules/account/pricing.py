from moceansdk.modules import AbstractClient


class Pricing(AbstractClient):

    def __init__(self, obj_auth, transmitter):
        super(Pricing, self).__init__(obj_auth, transmitter)
        self._required_fields = ['mocean-api-key', 'mocean-api-secret']

    def set_mcc(self, param):
        self._params['mocean-mcc'] = param
        return self

    def set_mnc(self, param):
        self._params['mocean-mnc'] = param
        return self

    def set_delimiter(self, param):
        self._params['mocean-delimiter'] = param
        return self

    def set_resp_format(self, param):
        self._params['mocean-resp-format'] = param
        return self

    def inquiry(self, params=None):
        if params is None:
            params = {}

        super(Pricing, self).create(params)
        self.create_final_params()
        self.is_required_field_set()

        return self._transmitter.get('/account/pricing', self._params)
