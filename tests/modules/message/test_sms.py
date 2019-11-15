import requests_mock

from moceansdk import RequiredFieldException
from moceansdk.modules.transmitter import Transmitter
from tests.testing_utils import TestingUtils


class TestSms(TestingUtils):
    def test_setter_method(self):
        sms = self.get_client_obj().sms

        sms.set_from("test from")
        self.assertIsNotNone(sms._params["mocean-from"])
        self.assertEqual("test from", sms._params["mocean-from"])

        sms.add_to("test to")
        self.assertIsNotNone(sms._params["mocean-to"])
        self.assertEqual("test to", sms._params["mocean-to"])
        sms.add_to("another to")
        self.assertEqual("test to,another to", sms._params["mocean-to"])

        sms.set_to("test to")
        self.assertIsNotNone(sms._params["mocean-to"])
        self.assertEqual("test to", sms._params["mocean-to"])

        sms.set_text("test text")
        self.assertIsNotNone(sms._params["mocean-text"])
        self.assertEqual("test text", sms._params["mocean-text"])

        sms.set_udh("test udh")
        self.assertIsNotNone(sms._params["mocean-udh"])
        self.assertEqual("test udh", sms._params["mocean-udh"])

        sms.set_coding("test coding")
        self.assertIsNotNone(sms._params["mocean-coding"])
        self.assertEqual("test coding", sms._params["mocean-coding"])

        sms.set_dlr_mask("test dlr mask")
        self.assertIsNotNone(sms._params["mocean-dlr-mask"])
        self.assertEqual("test dlr mask", sms._params["mocean-dlr-mask"])

        sms.set_dlr_url("test dlr url")
        self.assertIsNotNone(sms._params["mocean-dlr-url"])
        self.assertEqual("test dlr url", sms._params["mocean-dlr-url"])

        self.assertRaises(ValueError, sms.set_schedule, "testing schedule")
        sms.set_schedule("2019-02-01")
        self.assertIsNotNone(sms._params["mocean-schedule"])
        self.assertEqual("2019-02-01", sms._params["mocean-schedule"])

        sms.set_mclass("test mclass")
        self.assertIsNotNone(sms._params["mocean-mclass"])
        self.assertEqual("test mclass", sms._params["mocean-mclass"])

        sms.set_alt_dcs("test alt dcs")
        self.assertIsNotNone(sms._params["mocean-alt-dcs"])
        self.assertEqual("test alt dcs", sms._params["mocean-alt-dcs"])

        sms.set_charset("test charset")
        self.assertIsNotNone(sms._params["mocean-charset"])
        self.assertEqual("test charset", sms._params["mocean-charset"])

        sms.set_validity("test validity")
        self.assertIsNotNone(sms._params["mocean-validity"])
        self.assertEqual("test validity", sms._params["mocean-validity"])

        sms.set_resp_format("json")
        self.assertIsNotNone(sms._params["mocean-resp-format"])
        self.assertEqual("json", sms._params["mocean-resp-format"])

    @requests_mock.Mocker()
    def test_send_flash_sms(self, m):
        def request_callback(request, _context):
            self.verify_param_with(request.body, {'mocean-mclass': '1', 'mocean-alt-dcs': '1'})
            return self.get_response_string('message.json')

        self.mock_http_request(m, '/sms', request_callback)

        client = self.get_client_obj()
        client.flash_sms.send({
            'mocean-from': 'test from',
            'mocean-to': 'test to',
            'mocean-text': 'test text'
        })

        self.assertTrue(m.called)

    @requests_mock.Mocker()
    def test_json_send(self, m):
        def request_callback(request, _context):
            self.assertEqual(request.method, 'POST')
            self.verify_param_with(request.body, {'mocean-from': 'test from',
                                                  'mocean-to': 'test to',
                                                  'mocean-text': 'test text'})
            return self.get_response_string('message.json')

        self.mock_http_request(m, '/sms', request_callback)

        client = self.get_client_obj()
        res = client.sms.send({
            'mocean-from': 'test from',
            'mocean-to': 'test to',
            'mocean-text': 'test text'
        })

        self.assertEqual(res.__str__(), self.get_response_string('message.json'))
        self.__test_object(res)

        self.assertTrue(m.called)

    @requests_mock.Mocker()
    def test_xml_send(self, m):
        def request_callback(_request, _context):\
            return self.get_response_string('message.xml')

        self.mock_http_request(m, '/sms', request_callback, '1')

        client = self.get_client_obj(Transmitter({'version': '1'}))
        res = client.sms.send({
            'mocean-from': 'test from',
            'mocean-to': 'test to',
            'mocean-text': 'test text',
            'mocean-resp-format': 'xml'
        })

        self.assertEqual(res.__str__(), self.get_response_string('message.xml'))
        self.__test_object(res)

        # v2 test
        def request_callback_v2(_request, _context):\
            return self.get_response_string('message_v2.xml')

        self.mock_http_request(m, '/sms', request_callback_v2)

        client = self.get_client_obj()
        res = client.sms.send({
            'mocean-from': 'test from',
            'mocean-to': 'test to',
            'mocean-text': 'test text',
            'mocean-resp-format': 'xml'
        })

        self.assertEqual(res.__str__(), self.get_response_string('message_v2.xml'))
        self.__test_object(res)

        self.assertEqual(m.call_count, 2)

    @requests_mock.Mocker()
    def test_required_field_not_set(self, m):
        def request_callback(_request, _context):
            return self.get_response_string('message.json')

        self.mock_http_request(m, '/sms', request_callback)

        client = self.get_client_obj()
        try:
            client.sms.send()
            self.fail()
        except RequiredFieldException:
            pass

        self.assertFalse(m.called)

    def __test_object(self, sms_response):
        self.assertIsInstance(sms_response.toDict(), dict)
        self.assertEqual(sms_response.messages[0].status, '0')
        self.assertEqual(sms_response.messages[0].receiver, '60123456789')
        self.assertEqual(sms_response.messages[0].msgid, 'CPASS_restapi_C0000002737000000.0001')
