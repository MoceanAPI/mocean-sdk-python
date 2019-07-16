from unittest import TestCase

from moceansdk import Mccc, RequiredFieldException


class TestMccc(TestCase):
    def test_mccc_say(self):
        say = Mccc.say()

        try:
            say.get_request_data()
            self.fail()
        except RequiredFieldException:
            pass

        say.set_text('testing text')
        self.assertEqual('testing text', say.get_request_data()['text'])

        self.assertEqual('testing text2', Mccc.say('testing text2').get_request_data()['text'])

    def test_mccc_bridge(self):
        bridge = Mccc.bridge()

        try:
            bridge.get_request_data()
            self.fail()
        except RequiredFieldException:
            pass

        bridge.set_to('testing to')
        self.assertEqual('testing to', bridge.get_request_data()['to'])

        self.assertEqual('testing to2', Mccc.bridge('testing to2').get_request_data()['to'])

    def test_mccc_collect(self):
        collect = Mccc.collect()

        try:
            collect.get_request_data()
            self.fail()
        except RequiredFieldException:
            pass

        collect.set_event_url('testing event url')
        self.assertEqual('testing event url', collect.get_request_data()['event-url'])

        self.assertEqual('testing event url2', Mccc.collect('testing event url2').get_request_data()['event-url'])

    def test_mccc_play(self):
        play = Mccc.play()

        try:
            play.get_request_data()
            self.fail()
        except RequiredFieldException:
            pass

        play.set_files('testing file')
        self.assertEqual('testing file', play.get_request_data()['file'])

        self.assertEqual('testing file2', Mccc.play('testing file2').get_request_data()['file'])

    def test_mccc_sleep(self):
        sleep = Mccc.sleep()

        try:
            sleep.get_request_data()
            self.fail()
        except RequiredFieldException:
            pass

        sleep.set_duration(10000)
        self.assertEqual(10000, sleep.get_request_data()['duration'])

        self.assertEqual(20000, Mccc.sleep(20000).get_request_data()['duration'])
