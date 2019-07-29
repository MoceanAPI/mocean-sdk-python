from unittest import TestCase

from moceansdk import Mccc


class TestMccc(TestCase):
    def test_mccc_say(self):
        say = Mccc.say()
        say.set_text('testing text')
        self.assertEqual('testing text', say.get_request_data()['text'])

        self.assertEqual('testing text2', Mccc.say('testing text2').get_request_data()['text'])

    def test_mccc_bridge(self):
        bridge = Mccc.bridge()
        bridge.set_to('testing to')
        self.assertEqual('testing to', bridge.get_request_data()['to'])

        self.assertEqual('testing to2', Mccc.bridge('testing to2').get_request_data()['to'])

    def test_mccc_collect(self):
        collect = Mccc.collect()
        collect.set_event_url('testing event url')
        self.assertEqual('testing event url', collect.get_request_data()['event-url'])

        self.assertEqual('testing event url2', Mccc.collect('testing event url2').get_request_data()['event-url'])

    def test_mccc_play(self):
        play = Mccc.play()
        play.set_files('testing file')
        self.assertEqual('testing file', play.get_request_data()['file'])

        self.assertEqual('testing file2', Mccc.play('testing file2').get_request_data()['file'])

    def test_mccc_sleep(self):
        sleep = Mccc.sleep()
        sleep.set_duration(10000)
        self.assertEqual(10000, sleep.get_request_data()['duration'])

        self.assertEqual(20000, Mccc.sleep(20000).get_request_data()['duration'])
