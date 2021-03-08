from unittest import TestCase

from moceansdk import MoceanErrorException
from moceansdk.modules.command.mc import Mc
from moceansdk.modules.command.mc_builder import McBuilder


class TestMcBuilder(TestCase):
    def test_add(self):
        tg_send_text = Mc.telegram_send_text().set_from("test from").set_to("test to").set_content("test content")

        builder = McBuilder()
        builder.add(tg_send_text)
        self.assertEqual(1, len(builder.build()))
        self.assertEqual(tg_send_text.get_request_data(), builder.build()[0])

    def test_throw_exception_for_add_method_pass_in_non_mc_object(self):
        try:
            McBuilder().add('abc')
            self.fail()
        except MoceanErrorException:
            pass
