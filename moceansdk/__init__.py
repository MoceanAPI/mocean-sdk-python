#!/usr/bin/env python
# -*- coding: utf-8 -*-

name = "moceansdk"

class Client(object):
    
    def __init__(self,api_key,api_secret): 
        self.username = api_key
        self.password = api_secret
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
        from moceansdk.modules.Message.sms import SMS
        return SMS(self.obj_auth)
    @property
    def flashSms(self):
        from moceansdk.modules.Message.sms import SMS
        _sms = SMS(self.obj_auth)
        _sms.flash_message = 1
        return _sms

#     @property
#     def hlr(self):
#         from mocean.modules.Insight.hlr_query import Hlr_query
#         return Hlr_query(self.obj_auth)

    @property
    def balance(self):
        from moceansdk.modules.Account.balance import Balance
        return Balance(self.obj_auth)
    
    @property
    def price_list(self):
        from moceansdk.modules.Account.pricing import Pricing
        return Pricing(self.obj_auth)
    
    @property
    def message_status(self):
        from moceansdk.modules.Message.message_status import Messsage_status
        return Messsage_status(self.obj_auth)
    
    @property
    def verify_request(self):
        from moceansdk.modules.Message.verify_request import Verify_request
        return Verify_request(self.obj_auth)

    @property
    def verify_validate(self):
        from moceansdk.modules.Message.verify_validate import Verify_validate
        return Verify_validate(self.obj_auth)
    
    