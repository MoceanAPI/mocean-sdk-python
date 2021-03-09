from unittest import TestCase

from moceansdk import Basic


class TestBasic(TestCase):
    def setUp(self):
        self.basic = Basic()

    def test_set_api_key(self):
        self.basic.set_api_key('test api key')

        self.assertEqual(self.basic.get_params()[
                         'mocean-api-key'], 'test api key')

    def test_set_api_secret(self):
        self.basic.set_api_secret('test api secret')
        self.assertEqual(self.basic.get_params()[
                         'mocean-api-secret'], 'test api secret')

    def test_get_params(self):
        self.basic.set_api_key('test api key')
        self.basic.set_api_secret('test api secret')

        self.assertEqual(self.basic.get_params()[
                         'mocean-api-key'], 'test api key')
        self.assertEqual(self.basic.get_params()[
                         'mocean-api-secret'], 'test api secret')
