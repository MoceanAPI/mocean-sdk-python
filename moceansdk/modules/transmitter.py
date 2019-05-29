import requests

from moceansdk.exceptions import MoceanErrorException
from moceansdk.modules import ResponseFactory


class Transmitter(object):

    def __init__(self, options=None):
        self._options = self.default_options()

        if options is not None:
            self._options.update(dict(options))

    def default_options(self):
        return {
            "base_url": "https://rest.moceanapi.com",
            "version": "1"
        }

    def get(self, uri, params):
        return self.send('get', uri, params)

    def post(self, uri, params):
        return self.send('post', uri, params)

    def send(self, method, uri, params):
        params['mocean-medium'] = 'PYTHON-SDK'

        # use json if default not set
        if 'mocean-resp-format' not in params:
            params['mocean-resp-format'] = 'json'

        url = self._options['base_url'] + '/rest/' + self._options['version'] + uri
        res = None

        if method.lower() == 'get':
            res = requests.get(url, params=params or {})
        elif method.lower() == 'post':
            res = requests.post(url, data=params or {})

        return self.format_response(res.text, uri)

    def format_response(self, response_text, uri=None):
        raw_response = response_text

        # format for v1
        if uri is not None:
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
            raise MoceanErrorException(processed_response['err_msg'], processed_response)

        # format for v1
        if uri is not None:
            if uri == '/account/pricing':
                processed_response.destinations = processed_response.destinations.destination
            elif uri == '/sms':
                if not isinstance(processed_response.messages.message, list):
                    processed_response.messages.message = [processed_response.messages.message]
                processed_response.messages = processed_response.messages.message

        return processed_response.set_raw_response(raw_response)
