import json
import xmltodict
from dotmap import DotMap

from moceansdk import MoceanErrorException


class ResponseFactory:
    @staticmethod
    def create_object_from_raw_response(raw_response):
        try:
            dict_res = json.loads(raw_response, parse_float=lambda f: f, parse_int=lambda i: i)
        except Exception:
            try:
                dict_res = xmltodict.parse(raw_response, 'UTF-8')
                dict_res = dict_res['result']
            except Exception:
                raise MoceanErrorException('unable to parse response, ' + raw_response)

        return DotMapExtended(dict_res)


class DotMapExtended(DotMap):
    def __init__(self, *args, **kwargs):
        super(DotMapExtended, self).__init__(*args, **kwargs)
        self.__raw_response = ''

    def set_raw_response(self, raw_response):
        self.__raw_response = raw_response
        return self

    def toDict(self):
        dict_value = super(DotMapExtended, self).toDict()
        if '_DotMapExtended__raw_response' in dict_value:
            del dict_value['_DotMapExtended__raw_response']

        return dict_value

    def __str__(self):
        return self.__raw_response
