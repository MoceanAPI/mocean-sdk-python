from unittest import TestCase

from moceansdk import RequiredFieldException
from moceansdk.modules.voice.mccc_object.bridge import Bridge


class TestBridge(TestCase):
    def testParams(self):
        params = {
            'to': 'testing to',
            'action': 'dial'
        }
        self.assertEqual(params, Bridge(params).get_request_data())

        bridge = Bridge()
        bridge.set_to('testing to')

        self.assertEqual(params, bridge.get_request_data())

    def test_if_action_auto_defined(self):
        params = {
            'to': 'testing to'
        }

        self.assertEqual('dial', Bridge(params).get_request_data()['action'])

    def test_if_required_field_not_set(self):
        try:
            Bridge().get_request_data()
            self.fail()
        except RequiredFieldException:
            pass
