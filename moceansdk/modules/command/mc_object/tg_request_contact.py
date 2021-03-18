from builtins import super
from moceansdk.modules.command.mc_object import AbstractMc


class TgRequestContact(AbstractMc):

    def __init__(self):
        super().__init__()
        self.set_button_text('Share button')

    def action(self):
        return 'send-telegram'

    def required_key(self):
        return ('to', 'from')

    def set_to(self, _to, _contact_type='chat_id'):
        self._params['to'] = {}
        self._params['to']['type'] = _contact_type
        self._params['to']['id'] = _to
        return self

    def set_from(self, _from, _contact_type='bot_username'):
        self._params['from'] = {}
        self._params['from']['type'] = _contact_type
        self._params['from']['id'] = _from
        return self

    def set_content(self, _text):
        self._params['content'] = {}
        self._params['content']['type'] = 'text'
        self._params['content']['text'] = _text
        return self

    def set_button_text(self, _text):
        self._params['tg_keyboard'] = {}
        self._params['tg_keyboard']['button_request'] = 'contact'
        self._params['tg_keyboard']['button_text'] = _text
        return self
