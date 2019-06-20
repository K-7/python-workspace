import unittest

from core.constants import ErrorMessages
from problem1.processor import Processor


class TestPrblm1Processor(unittest.TestCase):
    def setUp(self):
        self.processor = Processor()

    def tearDown(self):
        self.processor = None

    def test_parser(self):
        name, message_txt = self.processor.parse_input('Air, "oaaawaala"')
        self.assertEqual(name, 'air')
        self.assertEqual(message_txt, 'oaaawaala')

        name, message_txt = self.processor.parse_input('Air, oaaawaala')
        self.assertEqual(name, 'air')
        self.assertEqual(message_txt, 'oaaawaala')

    def test_validator(self):
        isvalid, message = self.processor.validate('air', 'oaaawaala')
        self.assertEqual(isvalid, True)
        self.assertEqual(message, None)

        isvalid, message = self.processor.validate('airs', 'oaaawaala')
        self.assertEqual(isvalid, False)
        self.assertEqual(message, ErrorMessages.INVALID_KINGDOM.value.format('airs'))

        isvalid, message = self.processor.validate('land', '')
        self.assertEqual(isvalid, False)
        self.assertEqual(message, ErrorMessages.INVALID_MESSAGE.value)

    def test_processor(self):
        self.processor.cast_vote('air', 'oaaawaala')
        self.processor.cast_vote('land', 'a1d22n333a4444p')
        self.processor.cast_vote('ice', 'zmzmzmzaztzozh')

        self.processor.process_votes()
        ruler, allies = self.processor.voting_machine.kingdom_result('space', 2)

        self.assertEqual(ruler, 'Space')
        self.assertEqual(allies, 'Air, Land, Ice')
