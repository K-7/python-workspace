import unittest

from core.models import Kingdom


class TestKingdom(unittest.TestCase):
    def test_positive_creation(self):
        kingdom = Kingdom(
            name='LAND',
            emblem='Panda',
            ruler=True
        )
        self.assertEqual(type(kingdom), Kingdom)
        self.assertEqual(kingdom.display_name, 'Land')

    def test_negative_creation(self):
        with self.assertRaises(TypeError) as error:
            kingdom = Kingdom(
                name='LAND',
                emblem='Panda',
                ruler='STRING'
            )
        self.assertEqual(str(error.exception), 'ruler must be of type bool')
