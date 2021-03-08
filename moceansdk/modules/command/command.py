

import json
from moceansdk.exceptions import MoceanErrorException
from moceansdk.modules import AbstractClient, ResponseFactory
from moceansdk.modules.response_factory import DotMapExtended
from moceansdk.modules.command.mc_object import AbstractMc
from moceansdk.modules.command.mc_builder import McBuilder
from moceansdk.modules.command import channel

class Command(AbstractClient):

    def __init__(self, obj_auth, transmitter):
        super(Command, self).__init__(obj_auth, transmitter)
        self.channel = channel.TELEGRAM
        self._required_fields = ['mocean-api-key', 'mocean-api-secret','mocean-command']

    def set_event_url(self, event_url):
        self._params['mocean-event-url'] = event_url
        return self

    def set_command(self,command):
        if not isinstance(command, McBuilder):
            raise MoceanErrorException('Invalid command set, command must be instance of moceansdk.modules.command.mc_builder.McBuilder')

        self._params['mocean-command'] = json.dumps(command.build())
        return self

    def set_channel(self, channel):
        self.channel = channel
        return self

    def execute(self, params = None):
        if params == None:
            params = {}


        if 'mocean-event-url' in params:
            self._params['mocean-event-url'] = params['mocean-event-url']

        
        super(Command, self).create(params)
        self.create_final_params()
        
        if 'mocean-command' in params:
            if (not isinstance(params['mocean-command'],McBuilder)):
                raise MoceanErrorException('Invalid mocean-command set, command must be instance of moceansdk.modules.command.mc_builder.McBuilder')
     
            self._params['mocean-command'] = json.dumps(params['mocean-command'].build())
         
        
        if self.channel == channel.TELEGRAM:
            uri = '/send-message'
        else:
            raise MoceanErrorException('Channel %s not supported' %self.channel);

        response = self._transmitter.post(uri, self._params)
        return response
        
            




    

