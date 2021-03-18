from unittest import TestCase

from moceansdk.modules.command.mc import Mc


class TestMc(TestCase):
    def test_tg_send_photo(self):
        tg_send_photo = Mc.telegram_send_photo()
        tg_send_photo.set_from("from bot").set_to(
            "to chat").set_content("url", "text")

        self.assertEqual(
            'bot_username', tg_send_photo.get_request_data()['from']['type'])
        self.assertEqual(
            'from bot', tg_send_photo.get_request_data()['from']['id'])
        self.assertEqual(
            'chat_id', tg_send_photo.get_request_data()['to']['type'])
        self.assertEqual(
            'to chat', tg_send_photo.get_request_data()['to']['id'])

        self.assertEqual('photo', tg_send_photo.get_request_data()[
                         'content']['type'])
        self.assertEqual('url', tg_send_photo.get_request_data()[
                         'content']['rich_media_url'])
        self.assertEqual('text', tg_send_photo.get_request_data()[
                         'content']['text'])
