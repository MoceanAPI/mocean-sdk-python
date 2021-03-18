from unittest import TestCase

from moceansdk import RequiredFieldException
from moceansdk.modules.command.mc_object.send_sms import SendSMS


class TestTgSendText(TestCase):
    def testParams(self):
        params = {
            "action": "send-sms",
            "from": {
                "type": "phone_num",
                "id": "123456789"
            },
            "to": {
                "type": "phone_num",
                "id": "987654321"
            },
            "content": {
                "type": "text",
                "text": "test text"
            }
        }

        req = SendSMS()
        req.set_from("123456789")
        req.set_to("987654321")
        req.set_content("test text")

        self.assertEqual(params, req.get_request_data())

    def test_if_required_field_not_set(self):
        try:
            SendSMS().get_request_data()
            self.fail()
        except RequiredFieldException:
            pass
