from unittest import TestCase

from moceansdk.modules.voice.mc_object.record import Record


class TestRecord(TestCase):
    def test_if_action_auto_defined(self):
        self.assertEqual('record', Record().get_request_data()['action'])
