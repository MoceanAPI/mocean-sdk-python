import requests_mock

from moceansdk.modules.transmitter import Transmitter
from tests.testing_utils import TestingUtils


class TestPricing(TestingUtils):
    def test_setter_method(self):
        pricing = self.get_client_obj().pricing

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

    @requests_mock.Mocker()
    def test_json_inquiry(self, m):
        def request_callback(request, _context):
            self.assertEqual(request.method, 'GET')
            return self.get_response_string('price.json')

        self.mock_http_request(m, '/account/pricing', request_callback)

        client = self.get_client_obj()
        res = client.pricing.inquiry()
        self.assertEqual(res.__str__(), self.get_response_string('price.json'))
        self.__test_object(res)

        self.assertTrue(m.called)

    @requests_mock.Mocker()
    def test_xml_inquiry(self, m):
        def request_callback(_request, _context):
            return self.get_response_string('price.xml')

        self.mock_http_request(m, '/account/pricing', request_callback, '1')

        client = self.get_client_obj(Transmitter({'version': '1'}))
        res = client.pricing.inquiry({'mocean-resp-format': 'xml'})

        self.assertEqual(res.__str__(), self.get_response_string('price.xml'))
        self.__test_object(res)

        # v2 test
        def request_callback(_request, _context):
            return self.get_response_string('price_v2.xml')

        self.mock_http_request(m, '/account/pricing', request_callback)

        client = self.get_client_obj()
        res = client.pricing.inquiry({'mocean-resp-format': 'xml'})

        self.assertEqual(res.__str__(), self.get_response_string('price_v2.xml'))
        self.__test_object(res)

        self.assertEqual(m.call_count, 2)

    def __test_object(self, pricing_response):
        self.assertIsInstance(pricing_response.toDict(), dict)
        self.assertEqual(pricing_response.status, '0')
        self.assertEqual(len(pricing_response.destinations), 25)
        self.assertEqual(pricing_response.destinations[0].country, 'Default')
        self.assertEqual(pricing_response.destinations[0].operator, 'Default')
        self.assertEqual(pricing_response.destinations[0].mcc, 'Default')
        self.assertEqual(pricing_response.destinations[0].mnc, 'Default')
        self.assertEqual(pricing_response.destinations[0].price, '2.0000')
        self.assertEqual(pricing_response.destinations[0].currency, 'MYR')
