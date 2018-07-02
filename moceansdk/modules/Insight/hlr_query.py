from mocean.modules.abstract import MoceanFactory,Transmitter
class Hlr_query(MoceanFactory):
    
    def __init__(self,obj_auth):
        super(Hlr_query,self).__init__(obj_auth)
        self.required_fields = ['mocean-api-key','mocean-api-secret','mocean-to','mocean-hlr-url']
        
    def setTo(self,param):
        self.params['mocean-to'] = param
        pass
    
    def setHlrUrl(self,param):
        self.params['mocean-hlr-url'] = param
        pass
    
    def setRespFormat(self,param):
        self.params['mocean-resp-format'] = param
        pass
    
    def reset(self):
        self.params['mocean-to'] = None
        self.params['mocean-hlr-url'] = None
        self.params['mocean-resp-format'] = None
        
    def create(self,params = {}):
        self.reset()
        super(Hlr_query,self).create(params)
        return self
   
    def send(self):
        self.createFinalParams()
        if self.isRequiredFieldSet():
            response = Transmitter(url = self.domain+"/rest/1/hlr",method = "post",params = self.params)
            return self.createResponse(response.getResponse())