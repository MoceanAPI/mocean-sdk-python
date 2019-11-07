from moceansdk.modules.voice.mc_object import AbstractMc


class Collect(AbstractMc):
    def set_event_url(self, event_url):
        self._params['event-url'] = event_url
        return self

    def set_minimum(self, minimum):
        self._params['min'] = minimum
        return self

    def set_maximum(self, maximum):
        self._params['max'] = maximum
        return self

    def set_terminators(self, terminators):
        self._params['terminators'] = terminators
        return self

    def set_timeout(self, timeout):
        self._params['timeout'] = timeout
        return self

    def required_key(self):
        return ['event-url', 'min', 'max', 'timeout']

    def action(self):
        return 'collect'
