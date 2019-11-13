from moceansdk.modules.voice.mc_object.dial import Dial
from moceansdk.modules.voice.mc_object.collect import Collect
from moceansdk.modules.voice.mc_object.play import Play
from moceansdk.modules.voice.mc_object.say import Say
from moceansdk.modules.voice.mc_object.sleep import Sleep
from moceansdk.modules.voice.mc_object.record import Record


class Mc():
    @staticmethod
    def say(text=None):
        ins = Say()

        if text is not None:
            ins.set_text(text)

        return ins

    @staticmethod
    def play(file=None):
        ins = Play()

        if file is not None:
            ins.set_files(file)

        return ins

    @staticmethod
    def dial(to=None):
        ins = Dial()

        if to is not None:
            ins.set_to(to)

        return ins

    @staticmethod
    def collect(event_url=None):
        ins = Collect()

        if event_url is not None:
            ins.set_event_url(event_url)

        return ins

    @staticmethod
    def sleep(duration=None):
        ins = Sleep()

        if duration is not None:
            ins.set_duration(duration)

        return ins

    @staticmethod
    def record():
        return Record()