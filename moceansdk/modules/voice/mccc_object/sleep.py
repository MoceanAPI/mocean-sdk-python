from moceansdk.modules.voice.mccc_object import AbstractMccc


class Sleep(AbstractMccc):
    def set_duration(self, duration):
        self._params['duration'] = duration
        return self

    def required_key(self):
        return ['duration']

    def action(self):
        return 'sleep'
