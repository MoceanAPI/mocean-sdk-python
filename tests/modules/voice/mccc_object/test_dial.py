from unittest import TestCase

from moceansdk import RequiredFieldException
from moceansdk.modules.voice.mccc_object.dial import Dial


class TestDial(TestCase):
    def testParams(self):
        params = {
            'to': 'testing to',
            'action': 'dial',
            'from': 'callerid',
            'dial-sequentially': True,
        }
        self.assertEqual(params, Dial(params).get_request_data())

        dial = Dial()
        dial.set_to('testing to')
        dial.set_from('callerid')
        dial.set_dial_sequentially(True)

        self.assertEqual(params, dial.get_request_data())

    def test_if_action_auto_defined(self):
        params = {
            'to': 'testing to'
        }

        self.assertEqual('dial', Dial(params).get_request_data()['action'])

    def test_if_required_field_not_set(self):
        try:
            Dial().get_request_data()
            self.fail()
        except RequiredFieldException:
            pass
