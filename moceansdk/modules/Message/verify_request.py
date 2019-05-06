from moceansdk.modules.Message.charge_type import ChargeType
from moceansdk.modules.abstract import MoceanFactory,Transmitter

class Verify_request(MoceanFactory):
    
    def __init__(self,obj_auth):
        super(Verify_request,self).__init__(obj_auth)
        self.required_fields = ['mocean-api-key','mocean-api-secret','mocean-to','mocean-brand']
        self.chargeType = ChargeType.CHARGE_PER_CONVERSION
        pass
    
    def setTo(self,param):
        self.params['mocean-to'] = param
        return self
    
    def setBrand(self,param):
        self.params['mocean-brand'] = param
        return self
    
    def setFrom(self,param):
        self.params['mocean-from'] = param
        return self
    
    def setCodeLength(self,param):
        self.params['mocean-code-length'] = param
        return self
    
    def setTemplate(self,param):
        self.params['mocean-template'] = param
        return self
    
    def setPinValidity(self,param):
        self.params['mocean-pin-validity'] = param
        return self
    
    def setNextEventWait(self,param):
        self.params['mocean-next-event-wait'] = param
        return self
    
    def setRespFormat(self,param):
        self.params['mocean-resp-format'] = param
        return self

    def sendAs(self, charge_type):
        self.chargeType = charge_type
        return self
    
    def create(self,params):
        super(Verify_request,self).create(params)
        return self
    
    def send(self):
        self.createFinalParams()
        if self.isRequiredFieldSet():
            verifyRequestUrl = "/rest/1/verify/req"
            if self.chargeType == ChargeType.CHARGE_PER_ATTEMPT:
                verifyRequestUrl += "/sms"
            response = Transmitter(url = self.domain+verifyRequestUrl,method="post",params = self.params)
            return self.createResponse(response.getResponse())
    
    pass