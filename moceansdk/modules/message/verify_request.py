from moceansdk.modules.message.charge_type import ChargeType
from moceansdk.modules import AbstractClient


class VerifyRequest(AbstractClient):

    def __init__(self, obj_auth, transmitter):
        super(VerifyRequest, self).__init__(obj_auth, transmitter)
        self._required_fields = ['mocean-api-key', 'mocean-api-secret', 'mocean-to', 'mocean-brand']
        self.chargeType = ChargeType.CHARGE_PER_CONVERSION

    def set_to(self, param):
        self._params['mocean-to'] = param
        return self

    def set_brand(self, param):
        self._params['mocean-brand'] = param
        return self

    def set_from(self, param):
        self._params['mocean-from'] = param
        return self

    def set_code_length(self, param):
        self._params['mocean-code-length'] = param
        return self

    def set_template(self, param):
        self._params['mocean-template'] = param
        return self

    def set_pin_validity(self, param):
        self._params['mocean-pin-validity'] = param
        return self

    def set_next_event_wait(self, param):
        self._params['mocean-next-event-wait'] = param
        return self

    def set_resp_format(self, param):
        self._params['mocean-resp-format'] = param
        return self

    def send_as(self, charge_type):
        self.chargeType = charge_type
        return self

    def send(self, params=None):
        if params is None:
            params = {}

        super(VerifyRequest, self).create(params)
        self.create_final_params()
        self.is_required_field_set()

        verify_request_url = "/verify/req"
        if self.chargeType == ChargeType.CHARGE_PER_ATTEMPT:
            verify_request_url += "/sms"

        response = self._transmitter.post(verify_request_url, self._params)
        return response
