from moceansdk.modules.abstract import MoceanFactory,Transmitter
class Messsage_status(MoceanFactory):
    
    def __init__(self,obj_auth):
        super(Messsage_status,self).__init__(obj_auth)
        self.required_fields = ['mocean-api-key','mocean-api-secret','mocean-msgid']
        pass
    
    def setMsgid(self,param):
        self.params['mocean-msgid'] = param 
        pass
    
    def setRespFormat(self,param):
        self.param['mocean-resp-format'] = param
        pass
    
    def inquiry(self,params = {}):
        super(Messsage_status,self).create(params)   
        self.createFinalParams()
        if self.isRequiredFieldSet():
            response = Transmitter(url = self.domain+"/rest/1/report/message",method = "get",params = self.params)
            return self.createResponse(response.getResponse())
    pass