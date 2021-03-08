import json
from unittest import TestCase

import requests_mock

from moceansdk import RequiredFieldException, McBuilder, Mc
from tests.testing_utils import TestingUtils


class TestCommand(TestCase):
    def test_setter_method(self):
        command = TestingUtils.get_client_obj().command

        command.set_event_url('test url')
        self.assertIsNotNone(command._params['mocean-event-url'])
        self.assertEqual('test url', command._params['mocean-event-url'])

        command.set_mocean_command('test mocean command')
        self.assertIsNotNone(command._params['mocean-command'])
        self.assertEqual('test mocean command', command._params['mocean-command'])

    @requests_mock.Mocker()
    def test_json_execute(self, m):
        TestingUtils.intercept_mock_request(m, 'command.json', '/send-message', 'POST')

        client = TestingUtils.get_client_obj()
        res = client.command.execute({
            'mocean-to': 'test to',
            'mocean-command': 'test mocean call control commands'
        })

        self.assertEqual(res.__str__(), TestingUtils.get_response_string('command.json'))
        self.__test_object(res)

        self.assertTrue(m.called)

 

    def __test_object(self, command_response):
        self.assertIsInstance(command_response.toDict(), dict)
        self.assertEqual(command_response["status"], 0)
        self.assertEqual(command_response["session-uuid"], 'xxxxxx')
        self.assertEqual(command_response["mocean-command-resp"][0]["action"], 'xxxx-xxxx')
        self.assertEqual(command_response["mocean-command-resp"][0]["message-id"], 'xxxxxx')
        self.assertEqual(command_response["mocean-command-resp"][0]["mc-position"], 0)
        self.assertEqual(command_response["mocean-command-resp"][0]["total-message-segments"], 1)
