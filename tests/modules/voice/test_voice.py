import json
from unittest import TestCase
from mockito import when, ANY, verify, unstub

from moceansdk import RequiredFieldException, McccBuilder, Mccc
from moceansdk.modules.transmitter import Transmitter
from tests.testing_utils import TestingUtils


class TestVoice(TestCase):
    def setUp(self):
        self.client = TestingUtils.get_client_obj()

    def test_setter_method(self):
        voice = self.client.voice

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
        voice = self.client.voice
        voice.set_call_control_commands([{'action': 'say'}])
        self.assertIsNotNone(voice._params['mocean-call-control-commands'])
        self.assertEqual(json.dumps([{'action': 'say'}]), voice._params['mocean-call-control-commands'])

        voice = self.client.voice
        builder_params = McccBuilder().add(Mccc.say("hello world"))
        voice.set_call_control_commands(builder_params)
        self.assertIsNotNone(voice._params['mocean-call-control-commands'])
        self.assertEqual(json.dumps(builder_params.build()), voice._params['mocean-call-control-commands'])

        voice = self.client.voice
        mccc_params = Mccc.say('hello world')
        voice.set_call_control_commands(mccc_params)
        self.assertIsNotNone(voice._params['mocean-call-control-commands'])
        self.assertEqual(json.dumps(McccBuilder().add(mccc_params).build()),
                         voice._params['mocean-call-control-commands'])

    def test_call(self):
        transmitter_mock = Transmitter()
        when(transmitter_mock).send(ANY, ANY, ANY).thenReturn('testing only')

        client = TestingUtils.get_client_obj(transmitter_mock)

        # test is required field set
        try:
            client.voice.call()
            self.fail()
        except RequiredFieldException:
            pass

        self.assertEqual('testing only', client.voice.call({
            'mocean-to': 'test to',
            'mocean-call-control-commands': 'test call control commands'
        }))

        verify(transmitter_mock, times=1).send('get', '/voice/dial', ANY)

        unstub()

    def test_json_response(self):
        with open(TestingUtils.get_resource_file_path('voice.json'), 'r') as file_handler:
            file_content = ''.join(file_handler.read().splitlines())
            transmitter_mock = Transmitter()
            when(transmitter_mock).send(ANY, ANY, ANY).thenReturn(transmitter_mock.format_response(file_content))

            client = TestingUtils.get_client_obj(transmitter_mock)
            res = client.voice.call({
                'mocean-to': 'test to'
            })

            self.assertEqual(res.__str__(), file_content)
            self.__test_object(res)

        unstub()

    def test_xml_response(self):
        with open(TestingUtils.get_resource_file_path('voice.xml'), 'r') as file_handler:
            file_content = ''.join(file_handler.read().splitlines())
            transmitter_mock = Transmitter()
            when(transmitter_mock).send(ANY, ANY, ANY).thenReturn(
                transmitter_mock.format_response(file_content, '/voice/dial', True)
            )

            client = TestingUtils.get_client_obj(transmitter_mock)
            res = client.voice.call({
                'mocean-to': 'test to'
            })

            self.assertEqual(res.__str__(), file_content)
            self.__test_object(res)

        unstub()

    def __test_object(self, voice_response):
        self.assertIsInstance(voice_response.toDict(), dict)
        self.assertEqual(voice_response.status, '0')
        self.assertEqual(voice_response['session-uuid'], 'xxx-xxx-xxx-xxx')
        self.assertEqual(voice_response['call-uuid'], 'xxx-xxx-xxx-xxx')
