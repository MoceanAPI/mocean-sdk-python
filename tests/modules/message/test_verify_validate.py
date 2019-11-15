import requests_mock

from moceansdk import RequiredFieldException
from tests.testing_utils import TestingUtils


class TestVerifyValidate(TestingUtils):
    def test_setter_method(self):
        verify_validate = self.get_client_obj().verify_validate

        verify_validate.set_reqid("test reqid")
        self.assertIsNotNone(verify_validate._params["mocean-reqid"])
        self.assertEqual("test reqid", verify_validate._params["mocean-reqid"])

        verify_validate.set_code("test code")
        self.assertIsNotNone(verify_validate._params["mocean-code"])
        self.assertEqual("test code", verify_validate._params["mocean-code"])

        verify_validate.set_resp_format("json")
        self.assertIsNotNone(verify_validate._params["mocean-resp-format"])
        self.assertEqual("json", verify_validate._params["mocean-resp-format"])

    @requests_mock.Mocker()
    def test_json_send(self, m):
        def request_callback(request, _context):
            self.assertEqual(request.method, 'POST')
            self.verify_param_with(request.body, {'mocean-reqid': 'test reqid',
                                                  'mocean-code': 'test code'})
            return self.get_response_string('verify_code.json')

        self.mock_http_request(m, '/verify/check', request_callback)

        client = self.get_client_obj()
        res = client.verify_validate.send({
            'mocean-reqid': 'test reqid',
            'mocean-code': 'test code'
        })

        self.assertEqual(res.__str__(), self.get_response_string('verify_code.json'))
        self.__test_object(res)

        self.assertTrue(m.called)

    @requests_mock.Mocker()
    def test_xml_send(self, m):
        def request_callback(_request, _context):
            return self.get_response_string('verify_code.xml')

        self.mock_http_request(m, '/verify/check', request_callback)

        client = self.get_client_obj()
        res = client.verify_validate.send({
            'mocean-reqid': 'test reqid',
            'mocean-code': 'test code',
            'mocean-resp-format': 'xml'
        })

        self.assertEqual(res.__str__(), self.get_response_string('verify_code.xml'))
        self.__test_object(res)

        self.assertTrue(m.called)

    @requests_mock.Mocker()
    def test_required_field_not_set(self, m):
        def request_callback(_request, _context):
            return self.get_response_string('verify_code.json')

        self.mock_http_request(m, '/verify/check', request_callback)

        client = self.get_client_obj()
        try:
            client.verify_validate.send()
            self.fail()
        except RequiredFieldException:
            pass

        self.assertFalse(m.called)

    def __test_object(self, verify_validate_response):
        self.assertIsInstance(verify_validate_response.toDict(), dict)
        self.assertEqual(verify_validate_response.status, '0')
        self.assertEqual(verify_validate_response.reqid, 'CPASS_restapi_C0000002737000000.0002')
