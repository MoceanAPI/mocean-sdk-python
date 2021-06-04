import requests_mock

from moceansdk import RequiredFieldException
from moceansdk.modules.message.channel import Channel
from tests.testing_utils import TestingUtils


class TestVerifyRequest(TestingUtils):
    def test_setter_method(self):
        verify_request = self.get_client_obj().verify_request

        verify_request.set_to("test to")
        self.assertIsNotNone(verify_request._params["mocean-to"])
        self.assertEqual("test to", verify_request._params["mocean-to"])

        verify_request.set_brand("test brand")
        self.assertIsNotNone(verify_request._params["mocean-brand"])
        self.assertEqual("test brand", verify_request._params["mocean-brand"])

        verify_request.set_from("test from")
        self.assertIsNotNone(verify_request._params["mocean-from"])
        self.assertEqual("test from", verify_request._params["mocean-from"])

        verify_request.set_code_length("test code length")
        self.assertIsNotNone(verify_request._params["mocean-code-length"])
        self.assertEqual("test code length",
                         verify_request._params["mocean-code-length"])

        verify_request.set_template("test template")
        self.assertIsNotNone(verify_request._params["mocean-template"])
        self.assertEqual(
            "test template", verify_request._params["mocean-template"])

        verify_request.set_pin_validity("test pin validity")
        self.assertIsNotNone(verify_request._params["mocean-pin-validity"])
        self.assertEqual("test pin validity",
                         verify_request._params["mocean-pin-validity"])

        verify_request.set_next_event_wait("test next event wait")
        self.assertIsNotNone(verify_request._params["mocean-next-event-wait"])
        self.assertEqual("test next event wait",
                         verify_request._params["mocean-next-event-wait"])

        verify_request.set_resp_format("json")
        self.assertIsNotNone(verify_request._params["mocean-resp-format"])
        self.assertEqual("json", verify_request._params["mocean-resp-format"])

    @requests_mock.Mocker()
    def test_send_as_sms_channel(self, m):
        def request_callback(_request, _context):
            return self.get_response_string('send_code.json')

        self.mock_http_request(m, '/verify/req/sms', request_callback)

        client = self.get_client_obj()
        verify_request = client.verify_request
        self.assertEqual(verify_request._channel, Channel.AUTO)
        verify_request.send_as(Channel.SMS)
        self.assertEqual(verify_request._channel, Channel.SMS)
        verify_request.send({
            'mocean-to': 'testing to',
            'mocean-brand': 'testing brand'
        })

        self.assertTrue(m.called)

    @requests_mock.Mocker()
    def test_send_as_telegram_channel(self, m):
        TestingUtils.intercept_mock_request(
            m, 'send_code.json', '/verify/req/telegram', 'POST')

        client = TestingUtils.get_client_obj()
        verify_request = client.verify_request
        self.assertEqual(verify_request._channel, Channel.AUTO)
        verify_request.send_as(Channel.TELEGRAM)
        self.assertEqual(verify_request._channel, Channel.TELEGRAM)
        verify_request.send({
            'mocean-to': 'testing to',
            'mocean-brand': 'testing brand'
        })

        self.assertTrue(m.called)

    @requests_mock.Mocker()
    def test_resend(self, m):
        def request_callback(request, _context):
            self.assertEqual(request.method, 'POST')
            self.verify_param_with(request.body, {'mocean-reqid': 'testing req id'})
            return self.get_response_string('send_code.json')

        self.mock_http_request(m, '/verify/resend/sms', request_callback)

        client = self.get_client_obj()
        client.verify_request.resend({
            'mocean-reqid': 'testing req id'
        })

        self.assertTrue(m.called)

    @requests_mock.Mocker()
    def test_json_send(self, m):
        def request_callback(request, _context):
            self.assertEqual(request.method, 'POST')
            self.verify_param_with(request.body, {'mocean-to': 'test to',
                                                  'mocean-brand': 'test brand'})
            return self.get_response_string('send_code.json')

        self.mock_http_request(m, '/verify/req', request_callback)

        client = self.get_client_obj()
        res = client.verify_request.send({
            'mocean-to': 'test to',
            'mocean-brand': 'test brand'
        })

        self.assertEqual(res.__str__(), self.get_response_string('send_code.json'))
        self.__test_object(res)

        self.assertTrue(m.called)

    @requests_mock.Mocker()
    def test_xml_response(self, m):
        def request_callback(_request, _context):
            return self.get_response_string('send_code.xml')

        self.mock_http_request(m, '/verify/req', request_callback)

        client = self.get_client_obj()
        res = client.verify_request.send({
            'mocean-to': 'test to',
            'mocean-brand': 'test brand',
            'mocean-resp-format': 'xml'
        })

        self.assertEqual(res.__str__(), self.get_response_string('send_code.xml'))
        self.__test_object(res)

        self.assertTrue(m.called)

    @requests_mock.Mocker()
    def test_required_field_not_set(self, m):
        def request_callback(_request, _context):
            return self.get_response_string('send_code.json')

        self.mock_http_request(m, '/verify/req', request_callback)

        client = self.get_client_obj()
        try:
            client.verify_request.send()
            self.fail()
        except RequiredFieldException:
            pass

        self.assertFalse(m.called)

    def __test_object(self, verify_request_response):
        self.assertIsInstance(verify_request_response.toDict(), dict)
        self.assertEqual(verify_request_response.status, '0')
        self.assertEqual(verify_request_response.reqid,
                         'CPASS_restapi_C0000002737000000.0002')
