from moceansdk.modules.voice.mccc_object import AbstractMccc


class Play(AbstractMccc):
    def __init__(self, params=None):
        super(Play, self).__init__(params)

    def set_files(self, files):
        self._params['file'] = files
        return self

    def set_barge_in(self, barge_in):
        self._params['barge-in'] = barge_in
        return self

    def required_key(self):
        return ['file']

    def action(self):
        return 'play'
