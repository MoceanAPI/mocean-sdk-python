from unittest import TestCase

from moceansdk import RequiredFieldException
from moceansdk.modules.voice.mccc_object.sleep import Sleep


class TestSleep(TestCase):
    def testParams(self):
        params = {
            'duration': 10000,
            'action': 'sleep'
        }
        self.assertEqual(params, Sleep(params).get_request_data())

        sleep = Sleep()
        sleep.set_duration(10000)

        self.assertEqual(params, sleep.get_request_data())

    def test_if_action_auto_defined(self):
        params = {
            'duration': 10000,
            'barge-in': True
        }

        self.assertEqual('sleep', Sleep(params).get_request_data()['action'])

    def test_if_required_field_not_set(self):
        try:
            Sleep().get_request_data()
            self.fail()
        except RequiredFieldException:
            pass
