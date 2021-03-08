from moceansdk.modules.command.mc_object import AbstractMc
from moceansdk.modules.command.mc_object import contact_type

class RequestContact(AbstractMc):

    def __init__(self):
        super().__init__(self)
        self._params['tg_keyboard'] = {'tg_keyboard': {'button_text': 'Share Phone number', 'button_request': 'contact'}}

    def action(self):
        return 'send-telegram'
    
    def required_key(self):
        return ('to','from')

    def required_key(self):
        return ('from','to','content','tg_keyboard')

    def set_to(self,_to,_contact_type = 'chat_id'):
        self._params['to'] = {}
        self._params['to']['type'] = _contact_type
        self._params['to']['id'] = _to
        return self
    
    def set_from(self,_from, _contact_type = 'bot_username'):   
        self._params['from'] = {}     
        self._params['from']['type'] = _contact_type
        self._params['from']['id'] = _from
        return self

    def set_content(self,_text):
        self._params['content'] = {}
        self._params['content']['type'] = 'text'
        self._params['content']['text'] = _text
        return self

    def set_button(self,_text):
        self._params['tg_keyboard']['button_text'] = _text
        return self


