from moceansdk.modules import AbstractClient


class Sms(AbstractClient):

    def __init__(self, obj_auth, transmitter):
        super(Sms, self).__init__(obj_auth, transmitter)
        self._required_fields = ['mocean-api-key', 'mocean-api-secret', 'mocean-text', 'mocean-from', 'mocean-to']

    def set_from(self, param):
        self._params['mocean-from'] = param
        return self

    def set_to(self, param):
        self._params['mocean-to'] = param
        return self

    def set_text(self, param):
        self._params['mocean-text'] = param
        return self

    def set_udh(self, param):
        self._params['mocean-udh'] = param
        return self

    def set_coding(self, param):
        self._params['mocean-coding'] = param
        return self

    def set_dlr_mask(self, param):
        self._params['mocean-dlr-mask'] = param
        return self

    def set_dlr_url(self, param):
        self._params['mocean-dlr-url'] = param
        self._params['mocean-dlr-mask'] = '1'
        return self

    def set_schedule(self, param):
        import datetime
        try:
            datetime.datetime.strptime(param, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Incorrect schedule format. Example schedule 2018-01-01 (YYYY-MM-DD).")
        self._params['mocean-schedule'] = param
        return self

    def set_mclass(self, param):
        self._params['mocean-mclass'] = param
        return self

    def set_alt_dcs(self, param):
        self._params['mocean-alt-dcs'] = param
        return self

    def set_charset(self, param):
        self._params['mocean-charset'] = param
        return self

    def set_validity(self, param):
        self._params['mocean-validity'] = param
        return self

    def set_resp_format(self, param):
        self._params['mocean-resp-format'] = param
        return self

    def add_to(self, param):
        if self._params.get('mocean-to') is None:
            self._params['mocean-to'] = param
        else:
            self._params['mocean-to'] = self._params['mocean-to'] + "," + param
        return self

    def send(self, params=None):
        if params is None:
            params = {}

        super(Sms, self).create(params)
        self.create_final_params()
        self.is_required_field_set()

        response = self._transmitter.post('/sms', self._params)
        return response
