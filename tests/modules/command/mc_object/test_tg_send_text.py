from unittest import TestCase

from moceansdk import RequiredFieldException
from moceansdk.modules.command.mc_object.tg_send_text import TgSendText


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
            }
        }

        req = TgSendText()
        req.set_from("bot id")
        req.set_to("chat id")
        req.set_content("test text")

        self.assertEqual(params, req.get_request_data())

    def test_if_action_auto_defined(self):
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
            }
        }
        self.assertEqual('send-telegram', TgSendText(
            params).get_request_data()['action'])
        self.assertEqual('text', TgSendText(
            params).get_request_data()['content']['type'])

    def test_if_required_field_not_set(self):
        try:
            TgSendText().get_request_data()
            self.fail()
        except RequiredFieldException:
            pass
