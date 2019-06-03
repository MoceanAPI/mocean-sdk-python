from unittest import TestCase
from mockito import when, ANY, verify, unstub
from moceansdk.modules.transmitter import Transmitter
from tests.testing_utils import TestingUtils


class TestPricing(TestCase):
    def setUp(self):
        self.client = TestingUtils.get_client_obj()

    def test_setter_method(self):
        pricing = self.client.pricing

        pricing.set_mcc('test mcc')
        self.assertIsNotNone(pricing._params['mocean-mcc'])
        self.assertEqual('test mcc', pricing._params['mocean-mcc'])

        pricing.set_mnc('test mnc')
        self.assertIsNotNone(pricing._params['mocean-mnc'])
        self.assertEqual('test mnc', pricing._params['mocean-mnc'])

        pricing.set_delimiter('test delimiter')
        self.assertIsNotNone(pricing._params['mocean-delimiter'])
        self.assertEqual('test delimiter', pricing._params['mocean-delimiter'])

        pricing.set_resp_format('json')
        self.assertIsNotNone(pricing._params['mocean-resp-format'])
        self.assertEqual('json', pricing._params['mocean-resp-format'])

    def test_inquiry(self):
        transmitter_mock = Transmitter()
        when(transmitter_mock).send(ANY, ANY, ANY).thenReturn('testing only')

        client = TestingUtils.get_client_obj(transmitter_mock)
        self.assertEqual('testing only', client.pricing.inquiry())

        verify(transmitter_mock, times=1).send('get', '/account/pricing', ANY)

        unstub()

    def test_json_response(self):
        with open(TestingUtils.get_resource_file_path('price.json'), 'r') as file_handler:
            file_content = ''.join(file_handler.read().splitlines())
            transmitter_mock = Transmitter()
            when(transmitter_mock).send(ANY, ANY, ANY).thenReturn(transmitter_mock.format_response(file_content))

            client = TestingUtils.get_client_obj(transmitter_mock)
            res = client.pricing.inquiry()

            self.assertEqual(res.__str__(), file_content)
            self.__test_object(res)

        unstub()

    def test_xml_response(self):
        with open(TestingUtils.get_resource_file_path('price.xml'), 'r') as file_handler:
            file_content = ''.join(file_handler.read().splitlines())
            transmitter_mock = Transmitter({'version': '1'})
            when(transmitter_mock).send(ANY, ANY, ANY).thenReturn(
                transmitter_mock.format_response(file_content, '/account/pricing', True)
            )

            client = TestingUtils.get_client_obj(transmitter_mock)
            res = client.pricing.inquiry()

            self.assertEqual(res.__str__(), file_content)
            self.__test_object(res)

        unstub()

        with open(TestingUtils.get_resource_file_path('price_v2.xml'), 'r') as file_handler:
            file_content = ''.join(file_handler.read().splitlines())
            transmitter_mock = Transmitter({'version': '2'})
            when(transmitter_mock).send(ANY, ANY, ANY).thenReturn(
                transmitter_mock.format_response(file_content, '/account/pricing', True)
            )

            client = TestingUtils.get_client_obj(transmitter_mock)
            res = client.pricing.inquiry()

            self.assertEqual(res.__str__(), file_content)
            self.__test_object(res)

        unstub()

    def __test_object(self, pricing_response):
        self.assertEqual(pricing_response.status, '0')
        self.assertEqual(len(pricing_response.destinations), 25)
        self.assertEqual(pricing_response.destinations[0].country, 'Default')
        self.assertEqual(pricing_response.destinations[0].operator, 'Default')
        self.assertEqual(pricing_response.destinations[0].mcc, 'Default')
        self.assertEqual(pricing_response.destinations[0].mnc, 'Default')
        self.assertEqual(pricing_response.destinations[0].price, '2.0000')
        self.assertEqual(pricing_response.destinations[0].currency, 'MYR')
