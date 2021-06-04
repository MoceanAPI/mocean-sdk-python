from unittest import TestCase

from moceansdk import MoceanErrorException
from moceansdk.modules.transmitter import Transmitter


class TestTransmitter(TestCase):
    def test_malformed_response(self):
        try:
            Transmitter().format_response("malform string")
            self.fail()
        except MoceanErrorException:
            pass

    def test_has_default_options(self):
        transmitter_mock = Transmitter()
        self.assertEqual(
            transmitter_mock._options['base_url'], 'https://rest.moceanapi.com')
        self.assertEqual(transmitter_mock._options['version'], '2')

    def test_custom_options(self):
        transmitter_mock = Transmitter({
            'base_url': 'test base url',
            'version': '2'
        })

        self.assertEqual(
            transmitter_mock._options['base_url'], 'test base url')
        self.assertEqual(transmitter_mock._options['version'], '2')
