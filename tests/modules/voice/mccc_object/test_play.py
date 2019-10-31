from unittest import TestCase

from moceansdk import RequiredFieldException
from moceansdk.modules.voice.mccc_object.play import Play


class TestPlay(TestCase):
    def testParams(self):
        params = {
            'file': 'testing file',
            'barge-in': True,
            'clear-digit-cache': True,
            'action': 'play'
        }
        self.assertEqual(params, Play(params).get_request_data())

        play = Play()
        play.set_files('testing file')
        play.set_barge_in(True)
        play.set_clear_digit_cache(True)

        self.assertEqual(params, play.get_request_data())

    def test_if_action_auto_defined(self):
        params = {
            'file': 'testing file',
            'barge-in': True
        }

        self.assertEqual('play', Play(params).get_request_data()['action'])

    def test_if_required_field_not_set(self):
        try:
            Play().get_request_data()
            self.fail()
        except RequiredFieldException:
            pass
