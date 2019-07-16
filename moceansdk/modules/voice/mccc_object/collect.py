from moceansdk.modules.voice.mccc_object import AbstractMccc


class Collect(AbstractMccc):
    def __init__(self, params=None):
        super(Collect, self).__init__(params)

        # default value
        if 'min' not in self._params:
            self._params['min'] = 1

        if 'max' not in self._params:
            self._params['max'] = 10

        if 'terminators' not in self._params:
            self._params['terminators'] = '#'

        if 'timeout' not in self._params:
            self._params['timeout'] = 5000

    def set_event_url(self, event_url):
        self._params['event-url'] = event_url
        return self

    def set_min(self, min):
        self._params['min'] = min
        return self

    def set_max(self, max):
        self._params['max'] = max
        return self

    def set_terminators(self, terminators):
        self._params['terminators'] = terminators
        return self

    def set_timeout(self, timeout):
        self._params['timeout'] = timeout
        return self

    def required_key(self):
        return ['event-url', 'min', 'max', 'terminators', 'timeout']

    def action(self):
        return 'collect'
