from unittest import TestCase
from mockito import when, ANY, verify, unstub

from moceansdk import RequiredFieldException
from moceansdk.modules.transmitter import Transmitter
from tests.testing_utils import TestingUtils


class TestMessageStatus(TestCase):
    def setUp(self):
        self.client = TestingUtils.get_client_obj()

    def test_setter_method(self):
        number_lookup = self.client.number_lookup

        number_lookup.set_to('test to')
        self.assertIsNotNone(number_lookup._params['mocean-to'])
        self.assertEqual('test to', number_lookup._params['mocean-to'])

        number_lookup.set_nl_url('test nl url')
        self.assertIsNotNone(number_lookup._params['mocean-nl-url'])
        self.assertEqual('test nl url', number_lookup._params['mocean-nl-url'])

        number_lookup.set_resp_format('json')
        self.assertIsNotNone(number_lookup._params['mocean-resp-format'])
        self.assertEqual('json', number_lookup._params['mocean-resp-format'])

    def test_inquiry(self):
        transmitter_mock = Transmitter()
        when(transmitter_mock).send(ANY, ANY, ANY).thenReturn('testing only')

        client = TestingUtils.get_client_obj(transmitter_mock)

        # test is required field set
        try:
            client.number_lookup.inquiry()
            self.fail()
        except RequiredFieldException:
            pass

        self.assertEqual('testing only', client.number_lookup.set_to('test to').inquiry())

        verify(transmitter_mock, times=1).send('post', '/nl', ANY)

        unstub()

    def test_json_response(self):
        with open(TestingUtils.get_resource_file_path('number_lookup.json'), 'r') as file_handler:
            file_content = ''.join(file_handler.read().splitlines())
            transmitter_mock = Transmitter()
            when(transmitter_mock).send(ANY, ANY, ANY).thenReturn(transmitter_mock.format_response(file_content))

            client = TestingUtils.get_client_obj(transmitter_mock)
            res = client.number_lookup.inquiry({
                'mocean-to': 'test to'
            })

            self.assertEqual(res.__str__(), file_content)
            self.__test_object(res)

        unstub()

    def test_xml_response(self):
        with open(TestingUtils.get_resource_file_path('number_lookup.xml'), 'r') as file_handler:
            file_content = ''.join(file_handler.read().splitlines())
            transmitter_mock = Transmitter()
            when(transmitter_mock).send(ANY, ANY, ANY).thenReturn(
                transmitter_mock.format_response(file_content, True)
            )

            client = TestingUtils.get_client_obj(transmitter_mock)
            res = client.number_lookup.inquiry({
                'mocean-to': 'test to'
            })

            self.assertEqual(res.__str__(), file_content)
            self.__test_object(res)

        unstub()

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
