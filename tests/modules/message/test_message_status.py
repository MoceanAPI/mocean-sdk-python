from unittest import TestCase
from mockito import when, ANY, verify, unstub
from moceansdk.modules.transmitter import Transmitter
from tests.testing_utils import TestingUtils


class TestMessageStatus(TestCase):
    def setUp(self):
        self.client = TestingUtils.get_client_obj()

    def test_setter_method(self):
        message_status = self.client.message_status

        message_status.set_msgid('test msgid')
        self.assertIsNotNone(message_status._params['mocean-msgid'])
        self.assertEqual('test msgid', message_status._params['mocean-msgid'])

        message_status.set_resp_format('json')
        self.assertIsNotNone(message_status._params['mocean-resp-format'])
        self.assertEqual('json', message_status._params['mocean-resp-format'])

    def test_inquiry(self):
        transmitter_mock = Transmitter()
        when(transmitter_mock).send(ANY, ANY, ANY).thenReturn('testing only')

        client = TestingUtils.get_client_obj(transmitter_mock)
        self.assertEqual('testing only', client.message_status.inquiry({
            'mocean-msgid': 'test msg id'
        }))

        verify(transmitter_mock, times=1).send('get', '/report/message', ANY)

        unstub()

    def test_json_response(self):
        with open(TestingUtils.get_resource_file_path('message_status.json'), 'r') as file_handler:
            file_content = ''.join(file_handler.read().splitlines())
            transmitter_mock = Transmitter()
            when(transmitter_mock).send(ANY, ANY, ANY).thenReturn(transmitter_mock.format_response(file_content))

            client = TestingUtils.get_client_obj(transmitter_mock)
            res = client.message_status.inquiry({
                'mocean-msgid': 'test msg id'
            })

            self.assertEqual(res.__str__(), file_content)
            self.__test_object(res)

        unstub()

    def test_xml_response(self):
        with open(TestingUtils.get_resource_file_path('message_status.xml'), 'r') as file_handler:
            file_content = ''.join(file_handler.read().splitlines())
            transmitter_mock = Transmitter()
            when(transmitter_mock).send(ANY, ANY, ANY).thenReturn(
                transmitter_mock.format_response(file_content)
            )

            client = TestingUtils.get_client_obj(transmitter_mock)
            res = client.message_status.inquiry({
                'mocean-msgid': 'test msg id'
            })

            self.assertEqual(res.__str__(), file_content)
            self.__test_object(res)

        unstub()

    def __test_object(self, message_status_response):
        self.assertEqual(message_status_response.status, '0')
        self.assertEqual(message_status_response.message_status, '5')
        self.assertEqual(message_status_response.msgid, 'CPASS_restapi_C0000002737000000.0001')
        self.assertEqual(message_status_response.credit_deducted, '0.0000')
