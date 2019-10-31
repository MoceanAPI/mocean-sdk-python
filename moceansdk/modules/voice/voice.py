import json
from moceansdk.modules import AbstractClient
from moceansdk.modules.voice.mccc_object import AbstractMccc
from moceansdk.modules.voice.mccc_builder import McccBuilder


class Voice(AbstractClient):

    def __init__(self, obj_auth, transmitter):
        super(Voice, self).__init__(obj_auth, transmitter)
        self._required_fields = ['mocean-api-key', 'mocean-api-secret', 'mocean-to']

    def set_to(self, to):
        self._params['mocean-to'] = to
        return self

    def set_call_event_url(self, call_event_url):
        self._params['mocean-call-event-url'] = call_event_url
        return self

    def set_call_control_commands(self, call_control_commands):
        if isinstance(call_control_commands, McccBuilder):
            self._params['mocean-call-control-commands'] = json.dumps(call_control_commands.build())
        elif isinstance(call_control_commands, AbstractMccc):
            self._params['mocean-call-control-commands'] = json.dumps([call_control_commands.get_request_data()])
        elif isinstance(call_control_commands, list):
            self._params['mocean-call-control-commands'] = json.dumps(call_control_commands)
        else:
            self._params['mocean-call-control-commands'] = call_control_commands

        return self

    def set_resp_format(self, param):
        self._params['mocean-resp-format'] = param
        return self

    def call(self, params=None):
        if params is None:
            params = {}

        if 'mocean-call-control-commands' in params:
            mccc = params['mocean-call-control-commands']
            del params['mocean-call-control-commands']
            self.set_call_control_commands(mccc)

        super(Voice, self).create(params)
        self.create_final_params()
        self.is_required_field_set()

        response = self._transmitter.post('/voice/dial', self._params)
        return response
