from moceansdk.modules.voice.mc_object import AbstractMc


class Dial(AbstractMc):
    def set_to(self, to):
        self._params['to'] = to
        return self

    def set_from(self, param):
        self._params['from'] = param
        return self

    def set_dial_sequentially(self, dial_sequentially):
        self._params['dial-sequentially'] = dial_sequentially
        return self

    def required_key(self):
        return ['to']

    def action(self):
        return 'dial'
