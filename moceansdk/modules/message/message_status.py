from moceansdk.modules import AbstractClient


class MessageStatus(AbstractClient):

    def __init__(self, obj_auth, transmitter):
        super(MessageStatus, self).__init__(obj_auth, transmitter)
        self._required_fields = ['mocean-api-key', 'mocean-api-secret', 'mocean-msgid']

    def set_msgid(self, param):
        self._params['mocean-msgid'] = param
        return self

    def set_resp_format(self, param):
        self._params['mocean-resp-format'] = param
        return self

    def inquiry(self, params=None):
        if params is None:
            params = {}

        super(MessageStatus, self).create(params)
        self.create_final_params()
        self.is_required_field_set()

        response = self._transmitter.get('/report/message', self._params)
        return response
