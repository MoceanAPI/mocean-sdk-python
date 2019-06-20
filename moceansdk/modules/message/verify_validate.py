from moceansdk.modules import AbstractClient


class VerifyValidate(AbstractClient):

    def __init__(self, obj_auth, transmitter):
        super(VerifyValidate, self).__init__(obj_auth, transmitter)
        self._required_fields = ['mocean-api-key', 'mocean-api-secret', 'mocean-reqid', 'mocean-code']

    def set_reqid(self, param):
        self._params['mocean-reqid'] = param
        return self

    def set_code(self, param):
        self._params['mocean-code'] = param
        return self

    def set_resp_format(self, param):
        self._params['mocean-resp-format'] = param
        return self

    def send(self, params=None):
        if params is None:
            params = {}

        super(VerifyValidate, self).create(params)
        self.create_final_params()
        self.is_required_field_set()

        response = self._transmitter.post('/verify/check', self._params)
        return response
