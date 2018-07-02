#!/usr/bin/env python
# -*- coding: utf-8 -*-

name = "moceansdk"

class Client(object):
    
    def __init__(self,**kwargs): 
        self.username = kwargs.get('api_key')
        self.password = kwargs.get('api_secret')
        pass
    
    
    def setApiKey(self,username):
        self.username = username
        pass
    
    def setApiSecret(self,password):
        self.password = password
        pass
    pass



class Mocean(object):
    
    def __init__(self,obj_auth:Client):
        if not isinstance(obj_auth,Client):
            raise Exception('Authdication pass into mocean must be client object.')
        
        elif obj_auth.username == None or obj_auth.password == None:
            raise Exception("Username and password can't be empty.")
        
        else:
            self.obj_auth = obj_auth
            
            pass
    
    @property
    def sms(self):
        from mocean.modules.Message.sms import SMS
        return SMS(self.obj_auth)
    @property
    def flashSms(self):
        from mocean.modules.Message.sms import SMS
        _sms = SMS(self.obj_auth)
        _sms.flash_message = 1
        return _sms

#     @property
#     def hlr(self):
#         from mocean.modules.Insight.hlr_query import Hlr_query
#         return Hlr_query(self.obj_auth)

    @property
    def balance(self):
        import modules.Account.balance as module 
        return module.Balance(self.obj_auth)
    
    @property
    def price_list(self):
        import modules.Account.pricing as module
        return module.Pricing(self.obj_auth)
    
    @property
    def message_status(self):
        import modules.Message.message_status as module
        return module.Messsage_status(self.obj_auth)
    
    @property
    def verify_request(self):
        import modules.Message.verify_request as module
        return module.Verify_request(self.obj_auth)

    @property
    def verify_validate(self):
        import modules.Message.verify_validate as module
        return module.Verify_validate(self.obj_auth)
    
    