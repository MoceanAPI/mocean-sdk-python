import requests_mock
from tests.testing_utils import TestingUtils
from moceansdk.exceptions import MoceanErrorException


class TestRecording(TestingUtils):
    @requests_mock.Mocker()
    def test_json_call(self, m):
        def request_callback(request, context):
            self.assertEqual(request.method, 'GET')
            self.verify_param_with(request.query, {'mocean-call-uuid': 'xxx-xxx-xxx-xxx'})
            context.headers['Content-Type'] = 'audio/mpeg'
            return self.get_response_string('recording.json')

        self.mock_http_request(m, '/voice/rec', request_callback)

        client = self.get_client_obj()
        recording = client.voice.recording('xxx-xxx-xxx-xxx')

        self.assertIsNotNone(recording.recording_buffer)
        self.assertEqual(recording.filename, 'xxx-xxx-xxx-xxx.mp3')

        self.assertTrue(m.called)

    @requests_mock.Mocker()
    def test_error_call(self, m):
        def request_callback(_request, _context):
            return self.get_response_string('error_response.json')

        self.mock_http_request(m, '/voice/rec', request_callback)

        client = self.get_client_obj()
        self.assertRaises(MoceanErrorException, client.voice.recording, 'xxx-xxx-xxx-xxx')

        self.assertTrue(m.called)
