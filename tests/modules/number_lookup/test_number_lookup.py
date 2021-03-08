from unittest import TestCase

import requests_mock

from moceansdk import RequiredFieldException
from tests.testing_utils import TestingUtils


class TestNumberLookup(TestCase):
    def test_setter_method(self):
        number_lookup = TestingUtils.get_client_obj().number_lookup

        number_lookup.set_to('test to')
        self.assertIsNotNone(number_lookup._params['mocean-to'])
        self.assertEqual('test to', number_lookup._params['mocean-to'])

        number_lookup.set_nl_url('test nl url')
        self.assertIsNotNone(number_lookup._params['mocean-nl-url'])
        self.assertEqual('test nl url', number_lookup._params['mocean-nl-url'])

        number_lookup.set_resp_format('json')
        self.assertIsNotNone(number_lookup._params['mocean-resp-format'])
        self.assertEqual('json', number_lookup._params['mocean-resp-format'])

    @requests_mock.Mocker()
    def test_json_inquiry(self, m):
        TestingUtils.intercept_mock_request(m, 'number_lookup.json', '/nl', 'POST')

        client = TestingUtils.get_client_obj()
        res = client.number_lookup.inquiry({
            'mocean-to': 'test to'
        })

        self.assertEqual(res.__str__(), TestingUtils.get_response_string('number_lookup.json'))
        self.__test_object(res)

        self.assertTrue(m.called)

    @requests_mock.Mocker()
    def test_xml_inquiry(self, m):
        TestingUtils.intercept_mock_request(m, 'number_lookup.xml', '/nl', 'POST')

        client = TestingUtils.get_client_obj()
        res = client.number_lookup.inquiry({
            'mocean-to': 'test to',
            'mocean-resp-format': 'xml'
        })

        self.assertEqual(res.__str__(), TestingUtils.get_response_string('number_lookup.xml'))
        self.__test_object(res)

        self.assertTrue(m.called)

    @requests_mock.Mocker()
    def test_required_field_not_set(self, m):
        TestingUtils.intercept_mock_request(m, 'number_lookup.json', '/nl', 'POST')

        client = TestingUtils.get_client_obj()
        try:
            client.number_lookup.inquiry()
            self.fail()
        except RequiredFieldException:
            pass

        self.assertFalse(m.called)

    def __test_object(self, number_lookup_response):
        self.assertIsInstance(number_lookup_response.toDict(), dict)
        self.assertEqual(number_lookup_response.status, '0')
        self.assertEqual(number_lookup_response.msgid, 'CPASS_restapi_C00000000000000.0002')
        self.assertEqual(number_lookup_response.to, '60123456789')
        self.assertEqual(number_lookup_response.current_carrier.country, 'MY')
        self.assertEqual(number_lookup_response.current_carrier.name, 'U Mobile')
        self.assertEqual(number_lookup_response.current_carrier.network_code, '50218')
        self.assertEqual(number_lookup_response.current_carrier.mcc, '502')
        self.assertEqual(number_lookup_response.current_carrier.mnc, '18')
        self.assertEqual(number_lookup_response.original_carrier.country, 'MY')
        self.assertEqual(number_lookup_response.original_carrier.name, 'Maxis Mobile')
        self.assertEqual(number_lookup_response.original_carrier.network_code, '50212')
        self.assertEqual(number_lookup_response.original_carrier.mcc, '502')
        self.assertEqual(number_lookup_response.original_carrier.mnc, '12')
        self.assertEqual(number_lookup_response.ported, 'ported')
        self.assertEqual(number_lookup_response.reachable, 'reachable')
