import requests_mock

from tests.testing_utils import TestingUtils


class TestBalance(TestingUtils):
    def test_setter_method(self):
        balance = self.get_client_obj().balance
        balance.set_resp_format('json')
        self.assertIsNotNone(balance._params['mocean-resp-format'])
        self.assertEqual('json', balance._params['mocean-resp-format'])

    @requests_mock.Mocker()
    def test_json_inquiry(self, m):
        def request_callback(request, _context):
            self.assertEqual(request.method, 'GET')
            return self.get_response_string('balance.json')

        self.mock_http_request(m, '/account/balance', request_callback)

        client = self.get_client_obj()
        res = client.balance.inquiry()

        self.assertEqual(res.__str__(), self.get_response_string('balance.json'))
        self.__test_object(res)

        self.assertTrue(m.called)

    @requests_mock.Mocker()
    def test_xml_inquiry(self, m):
        def request_callback(_request, _context):
            return self.get_response_string('balance.xml')

        self.mock_http_request(m, '/account/balance', request_callback)

        client = self.get_client_obj()
        res = client.balance.inquiry({'mocean-resp-format': 'xml'})

        self.assertEqual(res.__str__(), self.get_response_string('balance.xml'))
        self.__test_object(res)

        self.assertTrue(m.called)

    def __test_object(self, balance_response):
        self.assertIsInstance(balance_response.toDict(), dict)
        self.assertEqual(balance_response.status, '0')
        self.assertEqual(balance_response.value, '100.0000')
