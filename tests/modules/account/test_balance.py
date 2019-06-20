from unittest import TestCase
from moceansdk.modules.transmitter import Transmitter
from mockito import when, ANY, verify, unstub
from tests.testing_utils import TestingUtils


class TestBalance(TestCase):
    def setUp(self):
        self.client = TestingUtils.get_client_obj()

    def test_setter_method(self):
        balance = self.client.balance
        balance.set_resp_format('json')
        self.assertIsNotNone(balance._params['mocean-resp-format'])
        self.assertEqual('json', balance._params['mocean-resp-format'])

    def test_inquiry(self):
        transmitter_mock = Transmitter()
        when(transmitter_mock).send(ANY, ANY, ANY).thenReturn('testing only')

        client = TestingUtils.get_client_obj(transmitter_mock)
        self.assertEqual('testing only', client.balance.inquiry())

        verify(transmitter_mock, times=1).send('get', '/account/balance', ANY)

        unstub()

    def test_json_response(self):
        with open(TestingUtils.get_resource_file_path('balance.json'), 'r') as file_handler:
            file_content = ''.join(file_handler.read().splitlines())
            transmitter_mock = Transmitter()
            when(transmitter_mock).send(ANY, ANY, ANY).thenReturn(transmitter_mock.format_response(file_content))

            client = TestingUtils.get_client_obj(transmitter_mock)
            res = client.balance.inquiry()

            self.assertEqual(res.__str__(), file_content)
            self.__test_object(res)

        unstub()

    def test_xml_response(self):
        with open(TestingUtils.get_resource_file_path('balance.xml'), 'r') as file_handler:
            file_content = ''.join(file_handler.read().splitlines())
            transmitter_mock = Transmitter()
            when(transmitter_mock).send(ANY, ANY, ANY).thenReturn(transmitter_mock.format_response(file_content, True))

            client = TestingUtils.get_client_obj(transmitter_mock)
            res = client.balance.inquiry()

            self.assertEqual(res.__str__(), file_content)
            self.__test_object(res)

        unstub()

    def __test_object(self, balance_response):
        self.assertIsInstance(balance_response.toDict(), dict)
        self.assertEqual(balance_response.status, '0')
        self.assertEqual(balance_response.value, '100.0000')
