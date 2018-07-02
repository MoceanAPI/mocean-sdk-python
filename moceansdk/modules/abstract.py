import requests
import sys
import re


class MoceanFactory(object):
    
    def __init__(self,obj_auth):
        self.params = dict(zip(['mocean-api-key','mocean-api-secret'],[obj_auth.username,obj_auth.password]))
        self.domain = "https://rest-api.moceansms.com"
        pass
    
    def create(self,params = {}):
        if isinstance(params,dict):
            if sys.version_info[0] == 3:
                self.params = {**self.params,**params}
            else:
                self.params.update(dict(params))
        pass
        
   
    def createFinalParams(self):
        tmp_params = dict()
        regex = re.compile('^mocean-', re.MULTILINE)
        for k,v in self.params.items():
            if v != None :
                new_key = k
                if regex.match(k) == None:
                    new_key = "mocean-"+k
                tmp_params[new_key] = v
        self.params = tmp_params
    
    def createResponse(self,response):
        if isinstance(self.params,dict):
            rest_format = self.params.get('mocean-resp-format')
            if rest_format != None and rest_format.lower() == 'json':
                import json
                return json.loads(response)
        return response
        
        
    def isRequiredFieldSet(self):
        if isinstance(self.required_fields,list):
            for x in self.required_fields:
                if self.params[x] == None:
                    raise Exception("%s is mandatory field"%(x))
    
        return True
    def reset(self):
        pass
    pass


class Transmitter(object):
    
    def __init__(self,method: str,url,params):
       
        self.url = url
        if method.lower() == 'post':
            self.response = self.__post(url, params)
    
        elif method.lower() == 'get':
            self.response = self.__get(url, params)
        
        elif method.lower() == 'put':
            self.response = self.__put(url, params)
        
        elif method.lower() == 'delete':
            self.response = self.delete(url,params)
        pass
    def send(self):
        pass
    
    def __get(self,url,params):
        return requests.get(url,params = params or {})
    
    def __post(self,url,params):
        return requests.post(url,data = params or {})
    
    def __put(self,url,params):
        return requests.put(url, data = params or {})

    def __delete(self,url,params):
        return requests.delete(url,data = params or {})
    
    def getResponse(self):
   
        if self.response.status_code == 401:
            raise Exception("Getting error %s from url %"%(self.response.status_code,self.url))
        elif self.response.status_code == 204:
            return None
        elif 200 <= self.response.status_code < 300:
            return self.response.text
        elif 400 <= self.response.status_code < 500:
            raise Exception("Getting error %s from url %"%(self.response.status_code,self.url))
        elif 500 <= self.response.status_code < 600:
            raise Exception("Getting error %s from url %"%(self.response.status_code,self.url))
