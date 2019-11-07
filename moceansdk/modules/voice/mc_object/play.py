from moceansdk.modules.voice.mc_object import AbstractMc


class Play(AbstractMc):
    def set_files(self, files):
        self._params['file'] = files
        return self

    def set_barge_in(self, barge_in):
        self._params['barge-in'] = barge_in
        return self

    def set_clear_digit_cache(self, clear_digit_cache):
        self._params['clear-digit-cache'] = clear_digit_cache
        return self

    def required_key(self):
        return ['file']

    def action(self):
        return 'play'
