import json

import requests_mock

from moceansdk import RequiredFieldException, McBuilder, Mc
from tests.testing_utils import TestingUtils


class TestVoice(TestingUtils):
    def test_setter_method(self):
        voice = self.get_client_obj().voice

        voice.set_to('test to')
        self.assertIsNotNone(voice._params['mocean-to'])
        self.assertEqual('test to', voice._params['mocean-to'])

        voice.set_event_url('test event url')
        self.assertIsNotNone(voice._params['mocean-event-url'])
        self.assertEqual('test event url', voice._params['mocean-event-url'])

        voice.set_mocean_command('test mocean command')
        self.assertIsNotNone(voice._params['mocean-command'])
        self.assertEqual('test mocean command',
                         voice._params['mocean-command'])

        voice.set_resp_format('json')
        self.assertIsNotNone(voice._params['mocean-resp-format'])
        self.assertEqual('json', voice._params['mocean-resp-format'])

        # test multiple call control commands
        voice = self.get_client_obj().voice
        voice.set_mocean_command([{'action': 'say'}])
        self.assertIsNotNone(voice._params['mocean-command'])
        self.assertEqual(json.dumps(
            [{'action': 'say'}]), voice._params['mocean-command'])

        voice = self.get_client_obj().voice
        builder_params = McBuilder().add(Mc.say("hello world"))
        voice.set_mocean_command(builder_params)
        self.assertIsNotNone(voice._params['mocean-command'])
        self.assertEqual(json.dumps(builder_params.build()),
                         voice._params['mocean-command'])

        voice = self.get_client_obj().voice
        mc_params = Mc.say('hello world')
        voice.set_mocean_command(mc_params)
        self.assertIsNotNone(voice._params['mocean-command'])
        self.assertEqual(json.dumps(McBuilder().add(mc_params).build()),
                         voice._params['mocean-command'])

    @requests_mock.Mocker()
    def test_json_call(self, m):
        def request_callback(request, _context):
            self.assertEqual(request.method, 'POST')
            self.verify_param_with(request.body, {'mocean-to': 'test to',
                                                  'mocean-command': 'test mocean call control commands'})
            return self.get_response_string('voice.json')

        self.mock_http_request(m, '/voice/dial', request_callback)

        client = self.get_client_obj()
        res = client.voice.call({
            'mocean-to': 'test to',
            'mocean-command': 'test mocean call control commands'
        })

        self.assertEqual(res.__str__(), self.get_response_string('voice.json'))
        self.__test_object(res)

        self.assertTrue(m.called)

    @requests_mock.Mocker()
    def test_xml_call(self, m):
        def request_callback(_request, _context):
            return self.get_response_string('voice.xml')

        self.mock_http_request(m, '/voice/dial', request_callback)

        client = self.get_client_obj()
        res = client.voice.call({
            'mocean-to': 'test to',
            'mocean-resp-format': 'xml'
        })

        self.assertEqual(res.__str__(), self.get_response_string('voice.xml'))
        self.__test_object(res)

        self.assertTrue(m.called)

    @requests_mock.Mocker()
    def test_json_hangup(self, m):
        def request_callback(request, _context):
            self.assertEqual(request.method, 'POST')
            self.verify_param_with(request.body, {'mocean-call-uuid': 'xxx-xxx-xxx-xxx'})
            return self.get_response_string('hangup.json')

        self.mock_http_request(m, '/voice/hangup', request_callback)

        client = self.get_client_obj()
        res = client.voice.hangup('xxx-xxx-xxx-xxx')

        self.assertEqual(res.__str__(), self.get_response_string('hangup.json'))
        self.assertEqual(res.status, '0')

        self.assertTrue(m.called)

    @requests_mock.Mocker()
    def test_xml_hangup(self, m):
        def request_callback(_request, _context):
            return self.get_response_string('hangup.xml')

        self.mock_http_request(m, '/voice/hangup', request_callback)

        client = self.get_client_obj()
        res = client.voice.hangup('xxx-xxx-xxx-xxx')

        self.assertEqual(res.__str__(), self.get_response_string('hangup.xml'))
        self.assertEqual(res.status, '0')

        self.assertTrue(m.called)

    # @requests_mock.Mocker()
    # def test_required_field_not_set(self, m):
    #     def request_callback(_request, _context):
    #         return self.get_response_string('voice.json')

    #     self.mock_http_request(m, '/voice/dial', request_callback)

    #     client = TestingUtils.get_client_obj()
    #     try:
    #         client.voice.call()
    #         self.fail()
    #     except RequiredFieldException:
    #         pass

    #     self.assertFalse(m.called)

    def __test_object(self, voice_response):
        self.assertIsInstance(voice_response.toDict(), dict)
        self.assertEqual(voice_response.calls[0].status, '0')
        self.assertEqual(voice_response.calls[0].receiver, '60123456789')
        self.assertEqual(
            voice_response.calls[0]['session_uuid'], 'xxx-xxx-xxx-xxx')
        self.assertEqual(
            voice_response.calls[0]['call_uuid'], 'xxx-xxx-xxx-xxx')
