import json
from moceansdk.modules import AbstractClient
from moceansdk.modules.command.mc_object import AbstractMc
from moceansdk.modules.command.mc_builder import McBuilder
from moceansdk.modules.command import channel


class Command(AbstractClient):

    def __init__(self, obj_auth, transmitter):
        super(Command, self).__init__(obj_auth, transmitter)
        self.channel = channel.TELEGRAM
        self._required_fields = ['mocean-api-key',
                                 'mocean-api-secret', 'mocean-command']

    def set_event_url(self, event_url):
        self._params['mocean-event-url'] = event_url
        return self

    def set_command(self, command):
        if isinstance(command, McBuilder):
            self._params['mocean-command'] = json.dumps(command.build())
        elif isinstance(command, AbstractMc):
            self._params['mocean-command'] = json.dumps(
                [command.get_request_data()])
        elif isinstance(command, list):
            self._params['mocean-command'] = json.dumps(command)
        else:
            self._params['mocean-command'] = command
        return self

    # def set_channel(self, channel):
    #     self.channel = channel
    #     return self

    def execute(self, params=None):
        if params == None:
            params = {}

        if 'mocean-command' in params:
            mc = params['mocean-command']
            del params['mocean-command']
            self.set_command(mc)

        super(Command, self).create(params)
        self.create_final_params()
        self.is_required_field_set()

        response = self._transmitter.post('/send-message', self._params)
        return response
