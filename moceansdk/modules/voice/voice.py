import json
from moceansdk.exceptions import MoceanErrorException
from moceansdk.modules import AbstractClient, ResponseFactory
from moceansdk.modules.response_factory import DotMapExtended
from moceansdk.modules.voice.mc_object import AbstractMc
from moceansdk.modules.voice.mc_builder import McBuilder


class Voice(AbstractClient):

    def __init__(self, obj_auth, transmitter):
        super(Voice, self).__init__(obj_auth, transmitter)
        self._required_fields = ['mocean-api-key', 'mocean-api-secret', 'mocean-to']

    def set_to(self, to):
        self._params['mocean-to'] = to
        return self

    def set_event_url(self, event_url):
        self._params['mocean-event-url'] = event_url
        return self

    def set_mocean_command(self, mocean_command):
        if isinstance(mocean_command, McBuilder):
            self._params['mocean-command'] = json.dumps(mocean_command.build())
        elif isinstance(mocean_command, AbstractMc):
            self._params['mocean-command'] = json.dumps([mocean_command.get_request_data()])
        elif isinstance(mocean_command, list):
            self._params['mocean-command'] = json.dumps(mocean_command)
        else:
            self._params['mocean-command'] = mocean_command

        return self

    def set_resp_format(self, param):
        self._params['mocean-resp-format'] = param
        return self

    def call(self, params=None):
        if params is None:
            params = {}

        if 'mocean-command' in params:
            mc = params['mocean-command']
            del params['mocean-command']
            self.set_mocean_command(mc)

        super(Voice, self).create(params)
        self.create_final_params()
        self.is_required_field_set()

        response = self._transmitter.post('/voice/dial', self._params)
        return response

    def hangup(self, call_uuid):
        self._required_fields = ['mocean-api-key', 'mocean-api-secret', 'mocean-call-uuid']

        super(Voice, self).create({'mocean-call-uuid': call_uuid})
        self.create_final_params()
        self.is_required_field_set()

        response = self._transmitter.post('/voice/hangup', self._params)
        return response

    def recording(self, call_uuid):
        self._required_fields = ['mocean-api-key', 'mocean-api-secret', 'mocean-call-uuid']

        super(Voice, self).create({'mocean-call-uuid': call_uuid})
        self.create_final_params()
        self.is_required_field_set()

        response = self._transmitter.send('get', '/voice/rec', self._params)

        if response.headers.get('Content-Type') == 'audio/mpeg':
            return DotMapExtended({'recording_buffer': response.content, 'filename': '%s.mp3' % call_uuid})

        # this method will raise exception if there's error
        processed_response = ResponseFactory.create_object_from_raw_response(response.text)
        raise MoceanErrorException(processed_response['err_msg'], processed_response.set_raw_response(response.text))
