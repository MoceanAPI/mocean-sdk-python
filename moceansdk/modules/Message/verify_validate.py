from mocean.modules.abstract import MoceanFactory,Transmitter

class Verify_validate(MoceanFactory):
    
    def __init__(self,obj_aut):
        super(Verify_validate,self).__init__(obj_auth)
        self.required_fields = ['mocean-api-key','mocean-api-secret','mocean-reqid','mocean-otp-code']
        pass

    def setReqid(self,param):
        self.params['mocean-reqid'] = param
        return self
    
    def setOtpCode(self,param):
        self.params['mocean-otp-code'] = param
        return self
    
    def setRespForamt(self,param):
        self.params['mocean-resp-format'] = param
        return self
    
    def create(self,params):
        super(Verify_validate,self).create(params)
        return self
    
    def send(self):
        self.createFinalParams()
        if self.isRequiredFieldSet():
            response = Transmitter(url = self.domain+"/rest/1/verify/check",method='post',params = self.params)
            return response.getResponse()
    pass
        