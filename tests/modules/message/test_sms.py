from unittest import TestCase
from mockito import when, ANY, verify, unstub
from moceansdk.modules.transmitter import Transmitter
from tests.testing_utils import TestingUtils


class TestSms(TestCase):
    def setUp(self):
        self.client = TestingUtils.get_client_obj()

    def test_setter_method(self):
        sms = self.client.sms

        sms.set_from("test from")
        self.assertIsNotNone(sms._params["mocean-from"])
        self.assertEqual("test from", sms._params["mocean-from"])

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

    def test_inquiry(self):
        transmitter_mock = Transmitter()
        when(transmitter_mock).send(ANY, ANY, ANY).thenReturn('testing only')

        client = TestingUtils.get_client_obj(transmitter_mock)
        self.assertEqual('testing only',
                         client.sms.send({
                             'mocean-from': 'test from',
                             'mocean-to': 'test to',
                             'mocean-text': 'test text'
                         }))

        verify(transmitter_mock, times=1).send('post', '/sms', ANY)

        unstub()

    def test_json_response(self):
        with open(TestingUtils.get_resource_file_path('message.json'), 'r') as file_handler:
            file_content = ''.join(file_handler.read().splitlines())
            transmitter_mock = Transmitter()
            when(transmitter_mock).send(ANY, ANY, ANY).thenReturn(transmitter_mock.format_response(file_content))

            client = TestingUtils.get_client_obj(transmitter_mock)
            res = client.sms.send({
                'mocean-from': 'test from',
                'mocean-to': 'test to',
                'mocean-text': 'test text'
            })

            self.assertEqual(res.__str__(), file_content)
            self.__test_object(res)

        unstub()

    def test_xml_response(self):
        with open(TestingUtils.get_resource_file_path('message.xml'), 'r') as file_handler:
            file_content = ''.join(file_handler.read().splitlines())
            transmitter_mock = Transmitter({'version': '1'})
            when(transmitter_mock).send(ANY, ANY, ANY).thenReturn(
                transmitter_mock.format_response(file_content, '/sms', True)
            )

            client = TestingUtils.get_client_obj(transmitter_mock)
            res = client.sms.send({
                'mocean-from': 'test from',
                'mocean-to': 'test to',
                'mocean-text': 'test text'
            })

            self.assertEqual(res.__str__(), file_content)
            self.__test_object(res)

        unstub()

        with open(TestingUtils.get_resource_file_path('message_v2.xml'), 'r') as file_handler:
            file_content = ''.join(file_handler.read().splitlines())
            transmitter_mock = Transmitter({'version': '2'})
            when(transmitter_mock).send(ANY, ANY, ANY).thenReturn(
                transmitter_mock.format_response(file_content, '/sms', True)
            )

            client = TestingUtils.get_client_obj(transmitter_mock)
            res = client.sms.send({
                'mocean-from': 'test from',
                'mocean-to': 'test to',
                'mocean-text': 'test text'
            })

            self.assertEqual(res.__str__(), file_content)
            self.__test_object(res)

        unstub()

    def __test_object(self, sms_response):
        self.assertEqual(sms_response.messages[0].status, '0')
        self.assertEqual(sms_response.messages[0].receiver, '60123456789')
        self.assertEqual(sms_response.messages[0].msgid, 'CPASS_restapi_C0000002737000000.0001')
