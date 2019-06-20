import unittest

from core.constants import ErrorMessages
from problem2.processor import Processor


class TestPrblm2Processor(unittest.TestCase):
    def setUp(self):
        self.processor = Processor()

    def tearDown(self):
        self.processor = None

    def test_parser(self):
        kingdom_list = self.processor.parse_input('Air Land')
        self.assertEqual(kingdom_list, ['air', 'land'])

        kingdom_list = self.processor.parse_input('Air')
        self.assertEqual(kingdom_list, ['air'])

    def test_validator(self):
        isvalid, message = self.processor.validate(['air', 'lands'])
        self.assertEqual(isvalid, False)
        self.assertEqual(message, ErrorMessages.INVALID_KINGDOM.value.format('lands'))

        isvalid, message = self.processor.validate(['air', 'air'])
        self.assertEqual(isvalid, False)
        self.assertEqual(message, ErrorMessages.DUPLICATE_MESSAGE.value)
