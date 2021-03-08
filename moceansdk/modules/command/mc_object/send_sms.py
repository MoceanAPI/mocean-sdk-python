from moceansdk.modules.command.mc_object import AbstractMc


class SendSMS(AbstractMc):

    def action(self):
        return 'send-sms'

    def required_key(self):
        return ('to', 'from', 'content')

    def set_to(self, _to, _contact_type='phone_num'):
        self._params['to'] = {}
        self._params['to']['type'] = _contact_type
        self._params['to']['id'] = _to
        return self

    def set_from(self, _from, _contact_type='phone_num'):
        self._params['from'] = {}
        self._params['from']['type'] = _contact_type
        self._params['from']['id'] = _from
        return self

    def set_content(self, _text=''):
        self._params['content'] = {'type': 'text'}
        self._params['content']['text'] = _text
        return self
