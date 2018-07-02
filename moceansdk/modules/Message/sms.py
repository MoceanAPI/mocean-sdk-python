from mocean.modules.abstract import MoceanFactory,Transmitter

class SMS(MoceanFactory):
    
    def __init__(self,obj_auth):
        super(SMS,self).__init__(obj_auth)
        self.required_fields = ['mocean-api-key','mocean-api-secret','mocean-text','mocean-from','mocean-to']
        self.flash_message = 0
        pass
    
    def setFrom(self,param):
        self.params['mocean-from'] = param
        pass
    
    def setTo(self,param):
        self.params['mocean-to'] = param
        pass
    
    def setText(self,param):
        self.params['mocean-text'] = param
        pass
    
    def setUdh(self,param):
        self.params['mocean-udh'] = param
        pass
    
    def setCoding(self,param):
        self.params['mocean-coding'] = param
        pass
    
    def setDlrMask(self,param):
        self.params['mocean-dlr-mask'] = param
        pass
    
    def setDlrUrl(self,param):
        self.params['mocean-dlr-url'] = param
        self.params['mocean-dlr-mask'] = '1'
        pass
    
    def setSchedule(self,param):
        import datetime
        try:
            datetime.datetime.strptime(param,"%Y-%m-%d")
        except ValueError:
            raise ValueError("Incorrect schedule format. Example schedule 2018-01-01 (YYYY-MM-DD).")
        self.params['mocean-schedule'] = param
        pass
    
    def setMclass(self,param):
        self.params['mocean-mclass'] = param
        pass
    
    def setAltDcs(self,param):
        self.params['mocean-alt-dcs'] = param
        pass
    
    def setCharset(self,param):
        self.params['mocean-charset'] = param
        pass
    
    def setValidity(self,param):
        self.params['mocean-validity'] = param
        pass
    
    def setRespFormat(self,param):
        self.params['mocean-resp-format'] = param
        pass
    
    def addTo(self,param):
        if self.params.get('mocean-to') == None:
            self.params['mocean-to'] = param
        else:
            self.params['mocean-to'] = self.params['mocean-to']+","+param
        pass
    
    def create(self, params:dict):
        self.reset()
        super(SMS,self).create(params)
        return self
        pass
    
    def reset(self):
        self.params['mocean-text'] = None
        self.params['mocean-udh'] = None
        self.params['mocean-coding'] = None
        self.params['mocean-dlr-mask'] = None
        self.params['mocean-dlr-url'] = None
        self.params['mocean-schedule'] = None
        self.params['mocean-mclass'] = None
        self.params['mocean-alt-dcs'] = None
        self.params['mocean-alt-charset'] = None
        self.params['mocean-validity'] = None
        self.params['mocean-from'] = None
        self.params['mocean-to'] = None
        self.params['mocean-resp-format'] = None
        pass 
    
    def send(self):
        self.createFinalParams()
        if self.isRequiredFieldSet():
            if self.flash_message == 1:
                self.params['mocean-mclass'] = 1
                self.params['mocean-alt-dcs'] = 1
            response = Transmitter(url = self.domain+"/rest/1/sms",method = "post",params = self.params)
            return self.createResponse(response.getResponse())
        pass

        
        
        