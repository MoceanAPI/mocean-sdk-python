from unittest import TestCase

from moceansdk import RequiredFieldException
from moceansdk.modules.command.mc_object.send_sms import SendSMS

class TestTgSendText(TestCase):
    def testParams(self):       
        params = {
            "action": "send-sms",
            "from": {
                "type": "bot_username",
                "id": "test id"
            },
            "to": {
                "type": "chat_id",
                "id": "test id"
            },
            "content": {
                "type": "text",
                "text": "test text"
            }
        }
      
        req = SendSMS()
        req.set_from("test from")
        req.set_to("test to")
        req.set_content("test content")

        self.assertEqual(params, req.get_request_data())


    def test_if_required_field_not_set(self):
        try:
            SendSMS().get_request_data()
            self.fail()
        except RequiredFieldException:
            pass
