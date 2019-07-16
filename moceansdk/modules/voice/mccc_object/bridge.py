from moceansdk.modules.voice.mccc_object import AbstractMccc


class Bridge(AbstractMccc):
    def __init__(self, params=None):
        super(Bridge, self).__init__(params)

    def set_to(self, to):
        self._params['to'] = to
        return self

    def required_key(self):
        return ['to']

    def action(self):
        return 'dial'
