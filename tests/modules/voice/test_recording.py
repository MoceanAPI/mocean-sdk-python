from unittest import TestCase
import requests_mock
from tests.testing_utils import TestingUtils
from moceansdk.exceptions import MoceanErrorException


class TestRecording(TestCase):
    @requests_mock.Mocker()
    def test_json_call(self, m):
        TestingUtils.intercept_mock_request(m, 'recording.json', '/voice/rec', 'GET', '2',
                                            {'Content-Type': 'audio/mpeg'})

        client = TestingUtils.get_client_obj()
        recording = client.voice.recording('xxx-xxx-xxx-xxx')

        self.assertIsNotNone(recording.recording_buffer)
        self.assertEqual(recording.filename, 'xxx-xxx-xxx-xxx.mp3')

        self.assertTrue(m.called)

    @requests_mock.Mocker()
    def test_error_call(self, m):
        TestingUtils.intercept_mock_request(
            m, 'error_response.json', '/voice/rec')

        client = TestingUtils.get_client_obj()
        self.assertRaises(MoceanErrorException,
                          client.voice.recording, 'xxx-xxx-xxx-xxx')

        self.assertTrue(m.called)
