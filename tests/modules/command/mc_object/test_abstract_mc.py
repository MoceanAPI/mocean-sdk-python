from unittest import TestCase

from moceansdk.modules.command.mc_builder import AbstractMc


class TestAbstractMc(TestCase):
    def test_throw_exception_if_calling_method_directly(self):
        try:
            AbstractMc().required_key()
            self.fail()
        except NotImplementedError:
            pass

        try:
            AbstractMc().action()
            self.fail()
        except NotImplementedError:
            pass
