from unittest import TestCase

from moceansdk import RequiredFieldException
from moceansdk.modules.command.mc_object.tg_send_animation import TgSendAnimation


class TestTgSendAnimation(TestCase):
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
                "type": "animation",
                "rich_media_url": "test url",
                "text": "test text"
            }
        }

        req = TgSendAnimation()
        req.set_from("bot id")
        req.set_to("chat id")
        req.set_content("test url", "test text")

        self.assertEqual(params, req.get_request_data())

    def test_if_required_field_not_set(self):
        try:
            TgSendAnimation().get_request_data()
            self.fail()
        except RequiredFieldException:
            pass
