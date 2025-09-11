from tests.testing_utils import TestingUtils

import requests_mock
import json

from moceansdk import RequiredFieldException
from moceansdk.modules.command.mc import Mc
from moceansdk.modules.command.mc_builder import McBuilder


class TestCommand(TestingUtils):
    def test_setter_method(self):
        command = TestingUtils.get_client_obj().command

        command.set_event_url('test url')
        self.assertIsNotNone(command._params['mocean-event-url'])
        self.assertEqual('test url', command._params['mocean-event-url'])

        command.set_command('test mocean command')
        self.assertIsNotNone(command._params['mocean-command'])
        self.assertEqual('test mocean command',
                         command._params['mocean-command'])

        # Test different set_command types
        command = TestingUtils.get_client_obj().command
        params = {
            "action": "send-telegram",
            "from": {
                "type": "bot_username",
                "id": "username"
            },
            "to": {
                "type": "chat_id",
                "id": "987654321"
            },
            "content": {
                "type": "text",
                "text": "test text"
            }
        }
        command.set_command([params])
        self.assertIsNotNone(command._params['mocean-command'])
        self.assertEqual(json.dumps(
            [params]), command._params['mocean-command'])

        command = TestingUtils.get_client_obj().command
        builder_params = McBuilder().add(Mc.telegram_send_text().set_from(
            'username').set_to('chat_id').set_content('test text'))
        command.set_command(builder_params)
        self.assertIsNotNone(command._params['mocean-command'])
        self.assertEqual(json.dumps(builder_params.build()),
                         command._params['mocean-command'])

        command = TestingUtils.get_client_obj().command
        mc_params = Mc.telegram_send_text().set_from(
            'username').set_to('chat_id').set_content('test text')
        command.set_command(mc_params)
        self.assertIsNotNone(command._params['mocean-command'])
        self.assertEqual(json.dumps(McBuilder().add(mc_params).build()),
                         command._params['mocean-command'])

    @requests_mock.Mocker()
    def test_json_execute(self, m):
        def request_callback(request, _context):
            self.assertEqual(request.method, 'POST')
            self.verify_param_with(request.body, {'mocean-to': 'test to',
                                                  'mocean-command': 'test mocean call control commands'})
            return self.get_response_string('command.json')

        self.mock_http_request(m, '/send-message', request_callback)

        client = TestingUtils.get_client_obj()
        res = client.command.execute({
            'mocean-to': 'test to',
            'mocean-command': 'test mocean call control commands'
        })

        self.assertEqual(
            res.__str__(), TestingUtils.get_response_string('command.json'))
        self.__test_object(res)

        self.assertTrue(m.called)

    @requests_mock.Mocker()
    def test_mocean_header_adder(self, m):
        def request_callback(request, _context):
            self.assertEqual(request.method, 'POST')
            self.verify_param_with(request.body, {'mocean-to': 'test to',
                                                  'mocean-command': 'test mocean call control commands'})
            return self.get_response_string('command.json')

        self.mock_http_request(m, '/send-message', request_callback)

        client = TestingUtils.get_client_obj()
        res = client.command.execute({
            'to': 'test to',
            'command': 'test mocean call control commands'
        })

        self.assertEqual(
            res.__str__(), TestingUtils.get_response_string('command.json'))
        self.__test_object(res)

        self.assertTrue(m.called)

    # @requests_mock.Mocker()
    # def test_required_field_not_set(self, m):
    #     def request_callback(_request, _context):
    #         return self.get_response_string('comamnd.json')

    #     client = TestingUtils.get_client_obj()
    #     try:
    #         client.command.execute()
    #         self.fail()
    #     except RequiredFieldException:
    #         pass

    #     self.assertFalse(m.called)

    def __test_object(self, command_response):
        self.assertIsInstance(command_response.toDict(), dict)
        self.assertEqual(command_response["status"], '0')
        self.assertEqual(command_response["session-uuid"], 'xxxxxx')
        self.assertEqual(
            command_response["mocean-command-resp"][0]["action"], 'xxxx-xxxx')
        self.assertEqual(
            command_response["mocean-command-resp"][0]["message-id"], 'xxxxxx')
        self.assertEqual(
            command_response["mocean-command-resp"][0]["mc-position"], '0')
        self.assertEqual(
            command_response["mocean-command-resp"][0]["total-message-segments"], '1')
