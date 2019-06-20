from parking_app.car import Car
from tests.test_base import TestBase


class TestCar(TestBase):

    def test_car_creation(self):
        car = Car(
            reg_no='DL-12-AA-9999',
            colour='White',
            slot_no=1
        )
        self.assertEqual(car.get_colour, 'White')
        self.assertEqual(car.get_reg_no, 'DL-12-AA-9999')
        self.assertEqual(car.get_slot, 1)

        with self.assertRaises(TypeError) as error:
            car = Car(
                reg_no='DL-12-AA-9999',
                colour='White',
                slot_no='a'
            )
        msg = str(error.exception)
        expected_msg = 'slot_no must be of type int'
        self.assertEqual(msg, expected_msg)

        with self.assertRaises(TypeError) as error:
            car = Car(
                reg_no='DL-12-AA-9999',
                colour=None,
                slot_no=1
            )
        msg = str(error.exception)
        expected_msg = '_Car__colour cannot be empty or NULL'
        self.assertEqual(msg, expected_msg)
