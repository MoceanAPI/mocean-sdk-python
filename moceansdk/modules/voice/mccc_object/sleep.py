from moceansdk.modules.voice.mccc_object import AbstractMccc


class Sleep(AbstractMccc):
    def __init__(self, params=None):
        super(Sleep, self).__init__(params)

    def set_duration(self, duration):
        self._params['duration'] = duration
        return self

    def set_barge_in(self, barge_in):
        self._params['barge-in'] = barge_in
        return self

    def required_key(self):
        return ['duration']

    def action(self):
        return 'sleep'
