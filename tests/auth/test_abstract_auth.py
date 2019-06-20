from unittest import TestCase

from moceansdk import AbstractAuth


class TestAbstractAuth(TestCase):
    def test_throw_exception_if_calling_method_directly(self):
        self.assertRaises(NotImplementedError, AbstractAuth().get_auth_method)
        self.assertRaises(NotImplementedError, AbstractAuth().get_params)
