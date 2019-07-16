from unittest import TestCase

from moceansdk import RequiredFieldException
from moceansdk.modules.voice.mccc_object.collect import Collect


class TestCollect(TestCase):
    def testParams(self):
        params = {
            'event-url': 'testing event url',
            'min': 1,
            'max': 10,
            'terminators': '#',
            'timeout': 10000,
            'action': 'collect'
        }

        self.assertEqual(params, Collect(params).get_request_data())

        collect = Collect()
        collect.set_event_url('testing event url')
        collect.set_min(1)
        collect.set_max(10)
        collect.set_terminators('#')
        collect.set_timeout(10000)

        self.assertEqual(params, collect.get_request_data())

    def test_if_action_auto_defined(self):
        params = {
            'event-url': 'testing event url',
            'min': 1,
            'max': 10,
            'terminators': '#',
            'timeout': 10000
        }

        self.assertEqual('collect', Collect(params).get_request_data()['action'])

    def test_if_required_field_not_set(self):
        try:
            Collect().get_request_data()
            self.fail()
        except RequiredFieldException:
            pass
