from unittest import TestCase

from moceansdk import Basic, RequiredFieldException, Client, MoceanErrorException, AbstractAuth


class TestClient(TestCase):
    def setUp(self):
        self.basic = Basic("test api key", "test api secret")

    def test_client_creation_error_when_no_api_key_or_api_secret(self):
        self.assertRaises(RequiredFieldException, Client, Basic())
        self.assertRaises(RequiredFieldException, Client, Basic("", ""))
        self.assertRaises(RequiredFieldException, Client, Basic("test api key", ""))
        self.assertRaises(RequiredFieldException, Client, Basic("", "test api secret"))
        self.assertRaises(RequiredFieldException, Client, Basic("test api key", None))
        self.assertRaises(RequiredFieldException, Client, Basic(None, "test api secret"))

    def test_able_to_construct_client_obj(self):
        try:
            Client(self.basic)
        except Exception as ex:
            self.fail(ex)

    def test_create_client_with_unsupported_auth(self):
        self.assertRaises(MoceanErrorException, Client, 'test_args')

        try:
            Client(DummyCredential())
            self.fail('created client with unsupported credential')
        except MoceanErrorException as ex:
            pass


class DummyCredential(AbstractAuth):
    def get_auth_method(self):
        return 'dummy'

    def get_params(self):
        pass
