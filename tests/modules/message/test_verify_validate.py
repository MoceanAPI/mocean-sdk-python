from unittest import TestCase
from mockito import when, ANY, verify, unstub
from moceansdk.modules.transmitter import Transmitter
from tests.testing_utils import TestingUtils


class TestVerifyValidate(TestCase):
    def setUp(self):
        self.client = TestingUtils.get_client_obj()

    def test_setter_method(self):
        verify_validate = self.client.verify_validate

        verify_validate.set_reqid("test reqid")
        self.assertIsNotNone(verify_validate._params["mocean-reqid"])
        self.assertEqual("test reqid", verify_validate._params["mocean-reqid"])

        verify_validate.set_code("test code")
        self.assertIsNotNone(verify_validate._params["mocean-code"])
        self.assertEqual("test code", verify_validate._params["mocean-code"])

        verify_validate.set_resp_format("json")
        self.assertIsNotNone(verify_validate._params["mocean-resp-format"])
        self.assertEqual("json", verify_validate._params["mocean-resp-format"])

    def test_inquiry(self):
        transmitter_mock = Transmitter()
        when(transmitter_mock).send(ANY, ANY, ANY).thenReturn('testing only')

        client = TestingUtils.get_client_obj(transmitter_mock)
        self.assertEqual('testing only',
                         client.verify_validate.send({
                             'mocean-reqid': 'test reqid',
                             'mocean-code': 'test code'
                         }))

        verify(transmitter_mock, times=1).send('post', '/verify/check', ANY)

        unstub()

    def test_json_response(self):
        with open(TestingUtils.get_resource_file_path('verify_code.json'), 'r') as file_handler:
            file_content = ''.join(file_handler.read().splitlines())
            transmitter_mock = Transmitter()
            when(transmitter_mock).send(ANY, ANY, ANY).thenReturn(transmitter_mock.format_response(file_content))

            client = TestingUtils.get_client_obj(transmitter_mock)
            res = client.verify_validate.send({
                'mocean-reqid': 'test reqid',
                'mocean-code': 'test code'
            })

            self.assertEqual(res.__str__(), file_content)
            self.__test_object(res)

        unstub()

    def test_xml_response(self):
        with open(TestingUtils.get_resource_file_path('verify_code.xml'), 'r') as file_handler:
            file_content = ''.join(file_handler.read().splitlines())
            transmitter_mock = Transmitter()
            when(transmitter_mock).send(ANY, ANY, ANY).thenReturn(
                transmitter_mock.format_response(file_content, True)
            )

            client = TestingUtils.get_client_obj(transmitter_mock)
            res = client.verify_validate.send({
                'mocean-reqid': 'test reqid',
                'mocean-code': 'test code'
            })

            self.assertEqual(res.__str__(), file_content)
            self.__test_object(res)

        unstub()

    def __test_object(self, verify_validate_response):
        self.assertEqual(verify_validate_response.status, '0')
        self.assertEqual(verify_validate_response.reqid, 'CPASS_restapi_C0000002737000000.0002')
        self.assertEqual(verify_validate_response.msgid, 'CPASS_restapi_C0000002737000000.0002')
        self.assertEqual(verify_validate_response.price, '0.35')
        self.assertEqual(verify_validate_response.currency, 'MYR')
