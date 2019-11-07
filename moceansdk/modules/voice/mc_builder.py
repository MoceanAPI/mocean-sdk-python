from moceansdk import MoceanErrorException
from moceansdk.modules.voice.mc_object import AbstractMc


class McBuilder():
    def __init__(self):
        self._mc = []

    def add(self, mc):
        if not isinstance(mc, AbstractMc):
            raise MoceanErrorException("mc_object must extend AbstractMc")
        self._mc.append(mc)
        return self

    def build(self):
        converted = []
        for mc in self._mc:
            converted.append(mc.get_request_data())
        return converted
