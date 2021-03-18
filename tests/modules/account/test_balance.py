from unittest import TestCase

import requests_mock

from tests.testing_utils import TestingUtils


class TestBalance(TestCase):
    def test_setter_method(self):
        balance = TestingUtils.get_client_obj().balance
        balance.set_resp_format('json')
        self.assertIsNotNone(balance._params['mocean-resp-format'])
        self.assertEqual('json', balance._params['mocean-resp-format'])

    @requests_mock.Mocker()
    def test_json_inquiry(self, m):
        TestingUtils.intercept_mock_request(
            m, 'balance.json', '/account/balance')

        client = TestingUtils.get_client_obj()
        res = client.balance.inquiry()

        self.assertEqual(
            res.__str__(), TestingUtils.get_response_string('balance.json'))
        self.__test_object(res)

        self.assertTrue(m.called)

    @requests_mock.Mocker()
    def test_xml_inquiry(self, m):
        TestingUtils.intercept_mock_request(
            m, 'balance.xml', '/account/balance')

        client = TestingUtils.get_client_obj()
        res = client.balance.inquiry({'mocean-resp-format': 'xml'})

        self.assertEqual(
            res.__str__(), TestingUtils.get_response_string('balance.xml'))
        self.__test_object(res)

        self.assertTrue(m.called)

    def __test_object(self, balance_response):
        self.assertIsInstance(balance_response.toDict(), dict)
        self.assertEqual(balance_response.status, '0')
        self.assertEqual(balance_response.value, '100.0000')
