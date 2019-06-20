from unittest import TestCase
from mockito import when, ANY, verify, unstub

from moceansdk import RequiredFieldException
from moceansdk.modules.message.channel import Channel
from moceansdk.modules.transmitter import Transmitter
from tests.testing_utils import TestingUtils


class TestVerifyRequest(TestCase):
    def setUp(self):
        self.client = TestingUtils.get_client_obj()

    def test_setter_method(self):
        verify_request = self.client.verify_request

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
        self.assertEqual("test code length", verify_request._params["mocean-code-length"])

        verify_request.set_template("test template")
        self.assertIsNotNone(verify_request._params["mocean-template"])
        self.assertEqual("test template", verify_request._params["mocean-template"])

        verify_request.set_pin_validity("test pin validity")
        self.assertIsNotNone(verify_request._params["mocean-pin-validity"])
        self.assertEqual("test pin validity", verify_request._params["mocean-pin-validity"])

        verify_request.set_next_event_wait("test next event wait")
        self.assertIsNotNone(verify_request._params["mocean-next-event-wait"])
        self.assertEqual("test next event wait", verify_request._params["mocean-next-event-wait"])

        verify_request.set_resp_format("json")
        self.assertIsNotNone(verify_request._params["mocean-resp-format"])
        self.assertEqual("json", verify_request._params["mocean-resp-format"])

    def test_send(self):
        transmitter_mock = Transmitter()
        when(transmitter_mock).send(ANY, ANY, ANY).thenReturn('testing only')

        client = TestingUtils.get_client_obj(transmitter_mock)

        # test is required field set
        try:
            client.verify_request.send()
            self.fail()
        except RequiredFieldException:
            pass

        self.assertEqual('testing only',
                         client.verify_request.set_to('test to').set_brand('test brand').send())

        verify(transmitter_mock, times=1).send('post', '/verify/req', ANY)

        unstub()

    def test_send_as_sms_channel(self):
        transmitter_mock = Transmitter()
        when(transmitter_mock).send(ANY, ANY, ANY).thenReturn('testing only')

        client = TestingUtils.get_client_obj(transmitter_mock)
        verify_request = client.verify_request
        self.assertEqual(verify_request._channel, Channel.AUTO)
        verify_request.send_as(Channel.SMS)
        self.assertEqual(verify_request._channel, Channel.SMS)
        verify_request.send({
            'mocean-to': 'testing to',
            'mocean-brand': 'testing brand'
        })

        verify(transmitter_mock, times=1).send('post', '/verify/req/sms', ANY)

        unstub()

    @staticmethod
    def test_resend():
        transmitter_mock = Transmitter()
        when(transmitter_mock).send(ANY, ANY, ANY).thenReturn('testing only')

        client = TestingUtils.get_client_obj(transmitter_mock)
        client.verify_request.resend({
            'mocean-reqid': 'testing req id'
        })

        verify(transmitter_mock, times=1).send('post', '/verify/resend/sms', ANY)

        unstub()

    def test_json_response(self):
        with open(TestingUtils.get_resource_file_path('send_code.json'), 'r') as file_handler:
            file_content = ''.join(file_handler.read().splitlines())
            transmitter_mock = Transmitter()
            when(transmitter_mock).send(ANY, ANY, ANY).thenReturn(transmitter_mock.format_response(file_content))

            client = TestingUtils.get_client_obj(transmitter_mock)
            res = client.verify_request.send({
                'mocean-to': 'test to',
                'mocean-brand': 'test brand'
            })

            self.assertEqual(res.__str__(), file_content)
            self.__test_object(res)

        unstub()

    def test_xml_response(self):
        with open(TestingUtils.get_resource_file_path('send_code.xml'), 'r') as file_handler:
            file_content = ''.join(file_handler.read().splitlines())
            transmitter_mock = Transmitter()
            when(transmitter_mock).send(ANY, ANY, ANY).thenReturn(
                transmitter_mock.format_response(file_content, True)
            )

            client = TestingUtils.get_client_obj(transmitter_mock)
            res = client.verify_request.send({
                'mocean-to': 'test to',
                'mocean-brand': 'test brand'
            })

            self.assertEqual(res.__str__(), file_content)
            self.__test_object(res)

        unstub()

    def __test_object(self, verify_request_response):
        self.assertIsInstance(verify_request_response.toDict(), dict)
        self.assertEqual(verify_request_response.status, '0')
        self.assertEqual(verify_request_response.reqid, 'CPASS_restapi_C0000002737000000.0002')
