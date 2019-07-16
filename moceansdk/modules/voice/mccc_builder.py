from moceansdk import MoceanErrorException
from moceansdk.modules.voice.mccc_object import AbstractMccc


class McccBuilder():
    def __init__(self):
        self._mccc = []

    def add(self, mccc):
        if not isinstance(mccc, AbstractMccc):
            raise MoceanErrorException("mccc_object must extend AbstractMccc")
        self._mccc.append(mccc)
        return self

    def build(self):
        converted = []
        for mccc in self._mccc:
            converted.append(mccc.get_request_data())
        return converted
