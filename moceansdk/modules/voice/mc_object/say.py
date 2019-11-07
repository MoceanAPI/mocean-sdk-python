from moceansdk.modules.voice.mc_object import AbstractMc


class Say(AbstractMc):
    def __init__(self, params=None):
        super(Say, self).__init__(params)

        # default value
        if 'language' not in self._params:
            self._params['language'] = 'en-US'

    def set_language(self, language):
        self._params['language'] = language
        return self

    def set_text(self, text):
        self._params['text'] = text
        return self

    def set_barge_in(self, barge_in):
        self._params['barge-in'] = barge_in
        return self

    def set_clear_digit_cache(self, clear_digit_cache):
        self._params['clear-digit-cache'] = clear_digit_cache
        return self

    def required_key(self):
        return ['text', 'language']

    def action(self):
        return 'say'
