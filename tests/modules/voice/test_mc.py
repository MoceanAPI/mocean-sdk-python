from unittest import TestCase

from moceansdk import Mc


class TestMc(TestCase):
    def test_mc_say(self):
        say = Mc.say()
        say.set_text('testing text')
        self.assertEqual('testing text', say.get_request_data()['text'])

        self.assertEqual('testing text2', Mc.say(
            'testing text2').get_request_data()['text'])

    def test_mc_dial(self):
        dial = Mc.dial()
        dial.set_to('testing to')
        self.assertEqual('testing to', dial.get_request_data()['to'])

        self.assertEqual('testing to2', Mc.dial(
            'testing to2').get_request_data()['to'])

    def test_mc_collect(self):
        collect = Mc.collect()
        collect.set_event_url('testing event url')
        collect.set_minimum(1)
        collect.set_maximum(10)
        collect.set_timeout(500)
        self.assertEqual('testing event url',
                         collect.get_request_data()['event-url'])

        collect = Mc.collect('testing event url2')
        collect.set_minimum(1)
        collect.set_maximum(10)
        collect.set_timeout(500)
        self.assertEqual('testing event url2',
                         collect.get_request_data()['event-url'])

    def test_mc_play(self):
        play = Mc.play()
        play.set_files('testing file')
        self.assertEqual('testing file', play.get_request_data()['file'])

        self.assertEqual('testing file2', Mc.play(
            'testing file2').get_request_data()['file'])

    def test_mc_sleep(self):
        sleep = Mc.sleep()
        sleep.set_duration(10000)
        self.assertEqual(10000, sleep.get_request_data()['duration'])

        self.assertEqual(20000, Mc.sleep(20000).get_request_data()['duration'])

    def test_mc_record(self):
        self.assertEqual('record', Mc.record().get_request_data()['action'])
