import unittest

from core.models import Kingdom
from core.models import Message
from core.models import MessageTable


class TestMessage(unittest.TestCase):
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

    def tearDown(self):
        self.kingdom1 = None
        self.kingdom2 = None

    def test_positive_creation(self):
        message = Message(
            sender=self.kingdom1,
            receiver=self.kingdom2,
            message='Test message'
        )
        self.assertEqual(type(message), Message)
        self.assertEqual(message.message, 'Test message')

    def test_negative_creation(self):
        with self.assertRaises(TypeError) as error:
            message = Message(
                sender=None,
                receiver=self.kingdom2,
                message='Test message'
            )
        self.assertEqual(str(error.exception), 'sender cannot be empty of NULL')

        with self.assertRaises(TypeError) as error:
            message = Message(
                sender={'sender': 'ken', 'receiver': 'gap', 'message': 'test'},
                receiver=self.kingdom2,
                message='Test message'
            )
        self.assertEqual(str(error.exception), 'sender must be of type Kingdom')

    def test_random_message_generation(self):
        message = MessageTable.get_random_message()
        self.assertEqual(type(message), str)
