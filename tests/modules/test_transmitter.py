from unittest import TestCase
from mockito import when, ANY, verify, unstub
from moceansdk import MoceanErrorException
from moceansdk.modules.transmitter import Transmitter


class TestTransmitter(TestCase):
    def test_get_method(self):
        transmitter_mock = Transmitter()
        when(transmitter_mock).send(ANY, ANY, ANY).thenReturn('testing only')

        transmitter_mock.get('test uri', {})
        verify(transmitter_mock, times=1).send('get', ANY, ANY)

        unstub()

    def test_post_method(self):
        transmitter_mock = Transmitter()
        when(transmitter_mock).send(ANY, ANY, ANY).thenReturn('testing only')

        transmitter_mock.post('test uri', {})
        verify(transmitter_mock, times=1).send('post', ANY, ANY)

        unstub()

    def test_malformed_response(self):
        try:
            Transmitter().format_response("malform string")
            self.fail()
        except MoceanErrorException:
            pass

    def test_has_default_options(self):
        transmitter_mock = Transmitter()
        self.assertEqual(transmitter_mock._options['base_url'], 'https://rest.moceanapi.com')
        self.assertEqual(transmitter_mock._options['version'], '1')

    def test_custom_options(self):
        transmitter_mock = Transmitter({
            'base_url': 'test base url',
            'version': '2'
        })

        self.assertEqual(transmitter_mock._options['base_url'], 'test base url')
        self.assertEqual(transmitter_mock._options['version'], '2')
