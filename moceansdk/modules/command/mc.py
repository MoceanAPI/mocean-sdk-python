from moceansdk.modules.command.mc_object import tg_send_text, tg_send_animation, tg_send_audio, tg_send_document, tg_send_photo, tg_send_video, tg_request_contact, send_sms


class Mc():

    @staticmethod
    def telegram_send_text():
        return tg_send_text.TgSendText()

    @staticmethod
    def telegram_send_animation():
        return tg_send_animation.TgSendAnimation()

    @staticmethod
    def telegram_send_audio():
        return tg_send_audio.TgSendAudio()

    @staticmethod
    def telegram_send_document():
        return tg_send_document.TgSendDocument()

    @staticmethod
    def telegram_send_photo():
        return tg_send_photo.TgSendPhoto()

    @staticmethod
    def telegram_send_video():
        return tg_send_video.TgSendVideo()

    @staticmethod
    def telegram_request_contact():
        return tg_request_contact.TgRequestContact()

    @staticmethod
    def send_sms():
        return send_sms.SendSMS()
