from moceansdk.modules.voice.mc_object import AbstractMc


class Record(AbstractMc):
    def required_key(self):
        return []

    def action(self):
        return 'record'
