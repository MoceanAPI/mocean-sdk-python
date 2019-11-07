from unittest import TestCase

from moceansdk import RequiredFieldException
from moceansdk.modules.voice.mc_object.say import Say


class TestSay(TestCase):
    def testParams(self):
        params = {
            'language': 'testing language',
            'text': 'testing text',
            'barge-in': True,
            'clear-digit-cache': True,
            'action': 'say'
        }
        self.assertEqual(params, Say(params).get_request_data())

        say = Say()
        say.set_language('testing language')
        say.set_text('testing text')
        say.set_barge_in(True)
        say.set_clear_digit_cache(True)

        self.assertEqual(params, say.get_request_data())

    def test_if_action_auto_defined(self):
        params = {
            'language': 'testing language',
            'text': 'testing text',
            'barge-in': True
        }

        self.assertEqual('say', Say(params).get_request_data()['action'])

    def test_if_required_field_not_set(self):
        try:
            Say().get_request_data()
            self.fail()
        except RequiredFieldException:
            pass
