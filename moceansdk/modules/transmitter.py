import requests

from moceansdk.exceptions import MoceanErrorException
from moceansdk.modules import ResponseFactory


class Transmitter(object):

    def __init__(self, options=None):
        self._options = self.default_options()

        if options is not None:
            self._options.update(dict(options))

    @staticmethod
    def default_options():
        return {
            "base_url": "https://rest.moceanapi.com",
            "version": "2",
            "request_session": requests.Session()
        }

    def get(self, uri, params):
        return self.send_and_decode_response('get', uri, params)

    def post(self, uri, params):
        return self.send_and_decode_response('post', uri, params)

    def send_and_decode_response(self, method, uri, params):
        res = self.send(method, uri, params)
        return self.format_response(res.text, uri, params['mocean-resp-format'] == 'xml')

    def send(self, method, uri, params):
        params['mocean-medium'] = 'PYTHON-SDK'

        # use json if default not set
        if 'mocean-resp-format' not in params:
            params['mocean-resp-format'] = 'json'

        url = self._options['base_url'] + \
            '/rest/' + self._options['version'] + uri
        res = None

        if method.lower() == 'get':
            res = self._options['request_session'].get(
                url, params=params or {})
        elif method.lower() == 'post':
            res = self._options['request_session'].post(url, data=params or {})

        cloned_res_before_close = res
        self._options['request_session'].close()

        return cloned_res_before_close

    def format_response(self, response_text, uri=None, is_xml=False):
        raw_response = response_text

        # format for v1
        if uri is not None and self._options['version'] == '1' and is_xml:
            if uri == '/account/pricing':
                response_text = response_text \
                    .replace("<data>", "<destinations>") \
                    .replace("</data>", "</destinations>")
            elif uri == '/sms':
                response_text = response_text \
                    .replace("<result>", "<result><messages>") \
                    .replace("</result>", "</messages></result>")

        processed_response = ResponseFactory.create_object_from_raw_response(
            response_text
            .replace("<verify_request>", "")
            .replace("</verify_request>", "")
            .replace("<verify_check>", "")
            .replace("</verify_check>", "")
        )

        if 'status' in processed_response and processed_response['status'] != '0':
            raise MoceanErrorException(
                processed_response['err_msg'], processed_response.set_raw_response(raw_response))

        # post process response
        if uri == '/account/pricing' and is_xml:
            processed_response.destinations = processed_response.destinations.destination
        elif uri == '/sms' and is_xml:
            if not isinstance(processed_response.messages.message, list):
                processed_response.messages.message = [
                    processed_response.messages.message]
            processed_response.messages = processed_response.messages.message
        elif uri == '/voice/dial' and is_xml:
            if not isinstance(processed_response.calls.call, list):
                processed_response.calls.call = [processed_response.calls.call]
            processed_response.calls = processed_response.calls.call

        return processed_response.set_raw_response(raw_response)
