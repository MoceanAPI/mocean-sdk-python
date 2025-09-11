import requests_mock

from moceansdk import RequiredFieldException
from tests.testing_utils import TestingUtils


class TestMessageStatus(TestingUtils):
    def test_setter_method(self):
        message_status = self.get_client_obj().message_status

        message_status.set_msgid('test msgid')
        self.assertIsNotNone(message_status._params['mocean-msgid'])
        self.assertEqual('test msgid', message_status._params['mocean-msgid'])

        message_status.set_resp_format('json')
        self.assertIsNotNone(message_status._params['mocean-resp-format'])
        self.assertEqual('json', message_status._params['mocean-resp-format'])

    @requests_mock.Mocker()
    def test_json_inqury(self, m):
        def request_callback(request, _context):
            self.assertEqual(request.method, 'GET')
            self.verify_param_with(request.query, {'mocean-msgid': 'test msg id'})
            return self.get_response_string('message_status.json')

        self.mock_http_request(m, '/report/message', request_callback)

        client = self.get_client_obj()
        res = client.message_status.inquiry({
            'mocean-msgid': 'test msg id'
        })

        self.assertEqual(res.__str__(), self.get_response_string('message_status.json'))
        self.__test_object(res)

        self.assertTrue(m.called)

    @requests_mock.Mocker()
    def test_xml_inquiry(self, m):
        def request_callback(_request, _context):
            return self.get_response_string('message_status.xml')

        self.mock_http_request(m, '/report/message', request_callback)

        client = self.get_client_obj()
        res = client.message_status.inquiry({
            'mocean-msgid': 'test msg id',
            'mocean-resp-format': 'xml'
        })

        self.assertEqual(res.__str__(), self.get_response_string('message_status.xml'))
        self.__test_object(res)

        self.assertTrue(m.called)

    # @requests_mock.Mocker()
    # def test_required_field_not_set(self, m):
    #     def request_callback(_request, _context):
    #         return self.get_response_string('message_status.json')

    #     self.mock_http_request(m, '/report/message', request_callback)

    #     client = self.get_client_obj()
    #     try:
    #         client.message_status.inquiry()
    #         self.fail()
    #     except RequiredFieldException:
    #         pass

    #     self.assertFalse(m.called)

    def __test_object(self, message_status_response):
        self.assertIsInstance(message_status_response.toDict(), dict)
        self.assertEqual(message_status_response.status, '0')
        self.assertEqual(message_status_response.message_status, '5')
        self.assertEqual(message_status_response.msgid,
                         'CPASS_restapi_C0000002737000000.0001')
        self.assertEqual(message_status_response.credit_deducted, '0.0000')
