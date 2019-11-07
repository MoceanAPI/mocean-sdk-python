from moceansdk import RequiredFieldException


class AbstractMc(object):
    def __init__(self, params=None):
        self._params = {}

        if params is not None:
            self._params = params

    def get_request_data(self):
        for required_key in self.required_key():
            if required_key not in self._params:
                raise RequiredFieldException("%s is mandatory field, %s" % (required_key, self.__class__.__name__))

        self._params['action'] = self.action()
        return self._params

    def required_key(self):
        raise NotImplementedError("AbstractMc is a abstract class")

    def action(self):
        raise NotImplementedError("AbstractMc is a abstract class")
