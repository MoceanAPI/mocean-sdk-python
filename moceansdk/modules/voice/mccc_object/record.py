from moceansdk.modules.voice.mccc_object import AbstractMccc


class Record(AbstractMccc):
    def required_key(self):
        return []

    def action(self):
        return 'record'
