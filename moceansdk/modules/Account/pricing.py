from moceansdk.modules.abstract import MoceanFactory,Transmitter

class Pricing(MoceanFactory):
    
    def __init__(self,obj_auth):
        super(Pricing,self).__init__(obj_auth)
        self.required_fields = ['mocean-api-key','mocean-api-secret']
        pass
    
    def setMcc(self,param):
        self.params['mocean-mcc'] = param
        return self
    
    def setMnc(self,param):
        self.params['mocean-mnc'] = param
        return self
    
    def setDelimiter(self,param):
        self.params['mocean-delimiter'] = param
        return self

    def setRespFormat(self,param):
        self.params['mocean-resp-format'] = param
        return self
    
    def reset(self):
        self.params['mocean-mcc'] = None
        self.params['mocean-mnc'] = None
        self.params['mocean-delimiter'] = None
        self.params['mocean-resp-format'] = None
    
    def create(self, params:dict):
        super(Pricing,self).create(params)
        return self
    
    def inquiry(self):
        self.createFinalParams()
        if self.isRequiredFieldSet():
            response = Transmitter(url = self.domain+"/rest/1/account/pricing",method = "get",params = self.params)
            return self.createResponse(response.getResponse())
    