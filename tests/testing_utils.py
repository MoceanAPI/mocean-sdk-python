import os

from moceansdk import Client, Basic


class TestingUtils(object):
    @staticmethod
    def get_client_obj(transmitter=None):
        return Client(Basic("test api key", "test api secret"), transmitter)

    @staticmethod
    def get_resource_file_path(file_name):
        cwd = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(cwd, 'resources/' + file_name)
