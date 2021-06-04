from moceansdk.modules.command.mc_object import AbstractMc


class TgSendDocument(AbstractMc):

    def action(self):
        return 'send-telegram'

    def required_key(self):
        return ('to', 'from', 'content')

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

    def set_content(self, _content, _text=''):
        self._params['content'] = {'type': 'document'}
        self._params['content']['rich_media_url'] = _content
        self._params['content']['text'] = _text
