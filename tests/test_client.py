from unittest import TestCase

from moceansdk import Basic, RequiredFieldException, Client, MoceanErrorException, AbstractAuth


class TestClient(TestCase):
    def setUp(self):
        self.basic = Basic(api_key="test api key", api_secret="test api secret")

    def test_client_creation_error_when_no_api_key_or_api_secret(self):
        self.assertRaises(RequiredFieldException, Client, Basic())
        self.assertRaises(RequiredFieldException, Client, Basic(api_key="", api_secret=""))
        self.assertRaises(RequiredFieldException, Client,
                          Basic("api_key=test api key", api_secret=""))
        self.assertRaises(RequiredFieldException, Client,
                          Basic(api_key="", api_secret="test api secret"))
        self.assertRaises(RequiredFieldException, Client,
                          Basic(api_key="test api key", api_secret=None))
        self.assertRaises(RequiredFieldException, Client,
                          Basic(api_key=None, api_secret="test api secret"))

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
        except MoceanErrorException:
            pass

    def test_able_to_construct_client_obj_with_token(self):
        try:
            Client(Basic(api_token="test api token"))
        except Exception as ex:
            self.fail(ex)


class DummyCredential(AbstractAuth):
    def get_auth_method(self):
        return 'dummy'

    def get_params(self):
        pass
