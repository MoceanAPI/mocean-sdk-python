from moceansdk.modules.abstract import MoceanFactory,Transmitter
class Balance(MoceanFactory):
    
    def __init__(self,obj_auth):
        super(Balance,self).__init__(obj_auth)
        self.required_fields = ['mocean-api-key','mocean-api-secret']
        pass
    
    def setRespFormat(self,param):
        self.params['mocean-resp-format'] = param
        return self
        pass
    
    def inquiry(self,params = {}):
        super(Balance,self).create(params)
        self.createFinalParams()
        if self.isRequiredFieldSet():
            response = Transmitter(url = self.domain+"/rest/1/account/balance",method = "get",params = self.params)
            return self.createResponse(response.getResponse())
    pass