import os
import sys

from moceansdk import Client, Basic
from moceansdk.modules import Transmitter

if (3, 0) <= sys.version_info < (4, 0):
    from urllib import parse as url_parser
elif (2, 0) <= sys.version_info < (3, 0):
    from urlparse import parse_qs as url_parser


class TestingUtils(object):
    @staticmethod
    def get_client_obj(transmitter=None):
        return Client(Basic("test api key", "test api secret"), transmitter)

    @staticmethod
    def get_resource_file_path(file_name):
        cwd = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(cwd, 'resources/' + file_name)

    @staticmethod
    def get_response_string(file_name):
        file_handler = open(
            TestingUtils.get_resource_file_path(file_name), 'r')
        file_content = ''.join(file_handler.read().splitlines())
        file_handler.close()
        return file_content

    @staticmethod
    def intercept_mock_request(m, file_name, uri, method='GET', version='2', headers=None):
        if headers is None:
            headers = {}

        m.request(method, Transmitter.default_options()['base_url'] + "/rest/" + version + uri,
                  text=TestingUtils.get_response_string(file_name), headers=headers)

    @staticmethod
    def convert_qs_to_dict(qs):
        if (2, 0) <= sys.version_info < (3, 0):
            return url_parser(qs)

        return url_parser.parse_qs(qs)
