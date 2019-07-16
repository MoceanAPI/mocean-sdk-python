from unittest import TestCase

from moceansdk.modules.voice.mccc_object import AbstractMccc


class TestAbstractMccc(TestCase):
    def test_throw_exception_if_calling_method_directly(self):
        try:
            AbstractMccc().required_key()
            self.fail()
        except NotImplementedError:
            pass

        try:
            AbstractMccc().action()
            self.fail()
        except NotImplementedError:
            pass
