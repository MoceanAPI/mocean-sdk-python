from moceansdk.modules.abstract import MoceanFactory, Transmitter


class NumberLookup(MoceanFactory):

    def __init__(self, obj_auth):
        super(NumberLookup, self).__init__(obj_auth)
        self.required_fields = ['mocean-api-key', 'mocean-api-secret', 'mocean-to']

    def setTo(self, param):
        self.params['mocean-to'] = param
        return self

    def setNlUrl(self, param):
        self.params['mocean-nl-url'] = param
        return self

    def setRespFormat(self, param):
        self.params['mocean-resp-format'] = param
        return self

    def reset(self):
        self.params['mocean-to'] = None
        self.params['mocean-nl-url'] = None
        self.params['mocean-resp-format'] = None

    def create(self, params={}):
        self.reset()
        super(NumberLookup, self).create(params)
        return self

    def inquiry(self):
        self.createFinalParams()
        if self.isRequiredFieldSet():
            response = Transmitter(url=self.domain + "/rest/1/nl", method="get", params=self.params)
            return self.createResponse(response.getResponse())
