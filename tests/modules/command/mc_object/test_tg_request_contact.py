from unittest import TestCase

from moceansdk import RequiredFieldException
from moceansdk.modules.command.mc_object.tg_request_contact import TgRequestContact


class TestTgSendText(TestCase):
    def testParams(self):
        params = {
            "action": "send-telegram",
            "from": {
                "type": "bot_username",
                "id": "bot id"
            },
            "to": {
                "type": "chat_id",
                "id": "chat id"
            },
            "content": {
                "type": "text",
                "text": "test text"
            },
            "tg_keyboard": {
                "button_text": "Share contact text",
                "button_request": "contact"
            }
        }

        req = TgRequestContact()
        req.set_from("bot id")
        req.set_to("chat id")
        req.set_content("test text")
        req.set_button_text("Share contact text")

        self.assertEqual(params, req.get_request_data())

    def test_if_required_field_not_set(self):
        try:
            TgRequestContact().get_request_data()
            self.fail()
        except RequiredFieldException:
            pass
