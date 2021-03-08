from unittest import TestCase

from moceansdk import RequiredFieldException
from moceansdk.modules.command.mc_object.tg_send_document import TgSendDocument

class TestTgSendText(TestCase):
    def testParams(self):       
        params = {
            "action": "send-telegram",
            "from": {
                "type": "bot_username",
                "id": "test id"
            },
            "to": {
                "type": "chat_id",
                "id": "test id"
            },
            "content": {
                "type": "document",
                "rich_media_url": "test url",
                "text": "test text"
            }
        }
      
        req = TgSendDocument()
        req.set_from("test from")
        req.set_to("test to")
        req.set_content("test url", "test content")

        self.assertEqual(params, req.get_request_data())



    def test_if_required_field_not_set(self):
        try:
            TgSendDocument().get_request_data()
            self.fail()
        except RequiredFieldException:
            pass
