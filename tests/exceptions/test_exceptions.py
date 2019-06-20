from unittest import TestCase
from moceansdk import Transmitter, MoceanErrorException
from moceansdk.modules.response_factory import DotMapExtended
from tests.testing_utils import TestingUtils


class TestException(TestCase):
    def test_raise_with_error_response(self):
        with open(TestingUtils.get_resource_file_path('error_response.json'), 'r') as file_handler:
            file_content = ''.join(file_handler.read().splitlines())

            try:
                Transmitter().format_response(file_content, True)
                self.fail()
            except MoceanErrorException as ex:
                self.assertEqual(ex.error_response.__str__(), file_content)
                self.assertIsInstance(ex.error_response, DotMapExtended)
                self.assertEqual(ex.error_response.status, '1')
