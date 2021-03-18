from unittest import TestCase

from moceansdk.modules.command.mc import Mc


class TestMc(TestCase):

    def test_tg_send_animation(self):
        tg_send_animation = Mc.telegram_send_animation()
        tg_send_animation.set_from("from bot").set_to(
            "to chat").set_content("url", "text")

        self.assertEqual(
            'bot_username', tg_send_animation.get_request_data()['from']['type'])
        self.assertEqual(
            'from bot', tg_send_animation.get_request_data()['from']['id'])
        self.assertEqual(
            'chat_id', tg_send_animation.get_request_data()['to']['type'])
        self.assertEqual(
            'to chat', tg_send_animation.get_request_data()['to']['id'])

        self.assertEqual('animation', tg_send_animation.get_request_data()[
                         'content']['type'])
        self.assertEqual('url', tg_send_animation.get_request_data()[
                         'content']['rich_media_url'])
        self.assertEqual('text', tg_send_animation.get_request_data()[
                         'content']['text'])

    def test_tg_send_audio(self):
        tg_send_audio = Mc.telegram_send_audio()
        tg_send_audio.set_from("from bot").set_to(
            "to chat").set_content("url", "text")

        self.assertEqual(
            'bot_username', tg_send_audio.get_request_data()['from']['type'])
        self.assertEqual(
            'from bot', tg_send_audio.get_request_data()['from']['id'])
        self.assertEqual(
            'chat_id', tg_send_audio.get_request_data()['to']['type'])
        self.assertEqual(
            'to chat', tg_send_audio.get_request_data()['to']['id'])

        self.assertEqual('audio', tg_send_audio.get_request_data()[
                         'content']['type'])
        self.assertEqual('url', tg_send_audio.get_request_data()[
                         'content']['rich_media_url'])
        self.assertEqual('text', tg_send_audio.get_request_data()[
                         'content']['text'])

    def test_tg_send_document(self):
        tg_send_document = Mc.telegram_send_document()
        tg_send_document.set_from("from bot").set_to(
            "to chat").set_content("url", "text")

        self.assertEqual(
            'bot_username', tg_send_document.get_request_data()['from']['type'])
        self.assertEqual(
            'from bot', tg_send_document.get_request_data()['from']['id'])
        self.assertEqual(
            'chat_id', tg_send_document.get_request_data()['to']['type'])
        self.assertEqual(
            'to chat', tg_send_document.get_request_data()['to']['id'])

        self.assertEqual('document', tg_send_document.get_request_data()[
                         'content']['type'])
        self.assertEqual('url', tg_send_document.get_request_data()[
                         'content']['rich_media_url'])
        self.assertEqual('text', tg_send_document.get_request_data()[
                         'content']['text'])

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

    def test_tg_send_video(self):
        tg_send_video = Mc.telegram_send_video()
        tg_send_video.set_from("from bot").set_to(
            "to chat").set_content("url", "text")

        self.assertEqual(
            'bot_username', tg_send_video.get_request_data()['from']['type'])
        self.assertEqual(
            'from bot', tg_send_video.get_request_data()['from']['id'])
        self.assertEqual(
            'chat_id', tg_send_video.get_request_data()['to']['type'])
        self.assertEqual(
            'to chat', tg_send_video.get_request_data()['to']['id'])

        self.assertEqual('video', tg_send_video.get_request_data()[
                         'content']['type'])
        self.assertEqual('url', tg_send_video.get_request_data()[
                         'content']['rich_media_url'])
        self.assertEqual('text', tg_send_video.get_request_data()[
                         'content']['text'])

    def test_tg_request_contact(self):
        tg_request_contact = Mc.telegram_request_contact()
        tg_request_contact.set_from("from bot").set_to(
            "to chat").set_content("hello!").set_button_text("button text")

        self.assertEqual(
            'bot_username', tg_request_contact.get_request_data()['from']['type'])
        self.assertEqual(
            'from bot', tg_request_contact.get_request_data()['from']['id'])
        self.assertEqual(
            'chat_id', tg_request_contact.get_request_data()['to']['type'])
        self.assertEqual(
            'to chat', tg_request_contact.get_request_data()['to']['id'])

        self.assertEqual('text', tg_request_contact.get_request_data()[
                         'content']['type'])

        self.assertEqual('hello!', tg_request_contact.get_request_data()[
                         'content']['text'])
        self.assertEqual('contact', tg_request_contact.get_request_data()[
                         'tg_keyboard']['button_request'])
        self.assertEqual('button text', tg_request_contact.get_request_data()[
                         'tg_keyboard']['button_text'])
