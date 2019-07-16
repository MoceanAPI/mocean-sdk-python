from unittest import TestCase

from moceansdk import McccBuilder, Mccc, MoceanErrorException


class TestMcccBuilder(TestCase):
    def test_add(self):
        play = Mccc.play('testing file')

        builder = McccBuilder()
        builder.add(play)
        self.assertEqual(1, len(builder.build()))
        self.assertEqual(play.get_request_data(), builder.build()[0])

        play.set_files('testing file2')
        builder.add(play)
        self.assertEqual(2, len(builder.build()))
        self.assertEqual(play.get_request_data(), builder.build()[1])

    def test_throw_exception_for_add_method_pass_in_non_mccc_object(self):
        try:
            McccBuilder().add('abc')
            self.fail()
        except MoceanErrorException:
            pass
