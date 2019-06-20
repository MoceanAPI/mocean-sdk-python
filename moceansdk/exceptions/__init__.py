class MoceanErrorException(Exception):
    def __init__(self, msg, error_response=None):
        if error_response is not None:
            super(MoceanErrorException, self).__init__(error_response['err_msg'])
            self._error_response = error_response
        else:
            super(MoceanErrorException, self).__init__(msg)

    @property
    def error_response(self):
        return self._error_response


class RequiredFieldException(MoceanErrorException):
    pass
