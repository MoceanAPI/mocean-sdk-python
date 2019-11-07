from moceansdk.modules.voice.mc_object import AbstractMc


class Sleep(AbstractMc):
    def set_duration(self, duration):
        self._params['duration'] = duration
        return self

    def required_key(self):
        return ['duration']

    def action(self):
        return 'sleep'
