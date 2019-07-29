import json
from unittest import TestCase

import requests_mock

from moceansdk import RequiredFieldException, McccBuilder, Mccc
from tests.testing_utils import TestingUtils


class TestVoice(TestCase):
    def test_setter_method(self):
        voice = TestingUtils.get_client_obj().voice

        voice.set_to('test to')
        self.assertIsNotNone(voice._params['mocean-to'])
        self.assertEqual('test to', voice._params['mocean-to'])

        voice.set_call_event_url('test call event url')
        self.assertIsNotNone(voice._params['mocean-call-event-url'])
        self.assertEqual('test call event url', voice._params['mocean-call-event-url'])

        voice.set_call_control_commands('test call control commands')
        self.assertIsNotNone(voice._params['mocean-call-control-commands'])
        self.assertEqual('test call control commands', voice._params['mocean-call-control-commands'])

        voice.set_resp_format('json')
        self.assertIsNotNone(voice._params['mocean-resp-format'])
        self.assertEqual('json', voice._params['mocean-resp-format'])

        # test multiple call control commands
        voice = TestingUtils.get_client_obj().voice
        voice.set_call_control_commands([{'action': 'say'}])
        self.assertIsNotNone(voice._params['mocean-call-control-commands'])
        self.assertEqual(json.dumps([{'action': 'say'}]), voice._params['mocean-call-control-commands'])

        voice = TestingUtils.get_client_obj().voice
        builder_params = McccBuilder().add(Mccc.say("hello world"))
        voice.set_call_control_commands(builder_params)
        self.assertIsNotNone(voice._params['mocean-call-control-commands'])
        self.assertEqual(json.dumps(builder_params.build()), voice._params['mocean-call-control-commands'])

        voice = TestingUtils.get_client_obj().voice
        mccc_params = Mccc.say('hello world')
        voice.set_call_control_commands(mccc_params)
        self.assertIsNotNone(voice._params['mocean-call-control-commands'])
        self.assertEqual(json.dumps(McccBuilder().add(mccc_params).build()),
                         voice._params['mocean-call-control-commands'])

    @requests_mock.Mocker()
    def test_json_call(self, m):
        TestingUtils.intercept_mock_request(m, 'voice.json', '/voice/dial')

        client = TestingUtils.get_client_obj()
        res = client.voice.call({
            'mocean-to': 'test to'
        })

        self.assertEqual(res.__str__(), TestingUtils.get_response_string('voice.json'))
        self.__test_object(res)

        self.assertTrue(m.called)

    @requests_mock.Mocker()
    def test_xml_call(self, m):
        TestingUtils.intercept_mock_request(m, 'voice.xml', '/voice/dial')

        client = TestingUtils.get_client_obj()
        res = client.voice.call({
            'mocean-to': 'test to',
            'mocean-resp-format': 'xml'
        })

        self.assertEqual(res.__str__(), TestingUtils.get_response_string('voice.xml'))
        self.__test_object(res)

        self.assertTrue(m.called)

    @requests_mock.Mocker()
    def test_required_field_not_set(self, m):
        TestingUtils.intercept_mock_request(m, 'voice.json', '/voice/dial')

        client = TestingUtils.get_client_obj()
        try:
            client.voice.call()
            self.fail()
        except RequiredFieldException:
            pass

        self.assertFalse(m.called)

    def __test_object(self, voice_response):
        self.assertIsInstance(voice_response.toDict(), dict)
        self.assertEqual(voice_response.status, '0')
        self.assertEqual(voice_response['session-uuid'], 'xxx-xxx-xxx-xxx')
        self.assertEqual(voice_response['call-uuid'], 'xxx-xxx-xxx-xxx')
