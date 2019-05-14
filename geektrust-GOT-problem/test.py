"""
python test.py -v
"""
import unittest
from models import Kingdom
from models import Message
from models import MessageTable
from models import BaseProcessor
from prblm1 import Processor as Processor1
from prblm2 import Processor as Processor2


class TestBase(unittest.TestCase):
    def setUp(self):
        self.kingdom1 = Kingdom(
            name='LAND',
            emblem='Panda',
            ruler=True
        )
        self.kingdom2 = Kingdom(
            name='WATER',
            emblem='Octopus',
            ruler=True
        )
        self.message_table = MessageTable()

        self.message1 = Message(
            sender=self.kingdom1,
            receiver=self.kingdom2,
            message=self.message_table.get_message()
        )

    def tearDown(self):
        self.kingdom1 = None
        self.kingdom2 = None
        self.message1 = None
        self.message_table = None

    def test_kingdom_class1(self):
        self.assertEqual(type(self.kingdom1), Kingdom)

    def test_kingdom_class2(self):
        with self.assertRaises(TypeError) as error:
            kingdom = Kingdom(
                name='LAND',
                emblem='Panda',
                ruler='STRING'
            )
        msg = str(error.exception)
        expected_msg = "ruler must be of type bool"
        self.assertEqual(msg, expected_msg)

    def test_message_class1(self):
        self.assertEqual(type(self.message1), Message)

    def test_abstract_class(self):
        with self.assertRaises(TypeError) as error:
            processor = BaseProcessor()
        msg = str(error.exception)
        expected_msg = "Can't instantiate abstract class BaseProcessor with abstract methods process_input"
        self.assertEqual(msg, expected_msg)


class TestPrblm1(TestBase):

    def test_processor1(self):
        processor = Processor1()
        output = processor.process_input('Who is the ruler of Southeros?')
        self.assertEqual(output, None)
        output = processor.process_input('Allies of Ruler?')
        self.assertEqual(output, None)
        t = processor.process_input('Air, "Let’s swing the sword together"')
        t = processor.process_input('Land, "Die or play the tame of thrones"')
        t = processor.process_input('Fire, "Drag on Martin!"')
        output = processor.process_input('Who is the ruler of Southeros?')
        ruler = processor.get_kingdom('space')
        air = processor.get_kingdom('Air')
        land = processor.get_kingdom('Land')
        fire = processor.get_kingdom('Fire')
        self.assertEqual(output.name, ruler.name)
        output = processor.process_input('Allies of Ruler?')
        self.assertEqual(len(output), 3)


class TestPrblm2(TestBase):

    def test_processor2(self):
        processor = Processor2()
        output = processor.process_input('Who is the ruler of Southeros?')
        self.assertEqual(output, None)
        output = processor.process_input('Allies of Ruler?')
        self.assertEqual(output, None)
        output = processor.process_input('Ice Space Air')
        tied_kingdoms = processor.check_for_tie(output)
        while tied_kingdoms:
            output = processor.process_input(tied_kingdoms)
            tied_kingdoms = processor.check_for_tie(output)
        self.assertEqual(type(output), dict)
        output = processor.process_input('Who is the ruler of Southeros?')
        self.assertNotEqual(output, None)


if __name__ == '__main__':
    unittest.main()
