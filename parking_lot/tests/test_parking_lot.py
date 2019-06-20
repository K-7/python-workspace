from parking_app.constants import ErrorMessages
from parking_app.constants import ResponseMessages
from tests.test_base import TestBase


class TestParkingLot(TestBase):
    def test_create_parking_lot(self):
        message = self.parking.create_parking_lot(2)
        self.assertEqual(message, ResponseMessages.PARKING_LOT_CREATED.value.format(2))
        with self.assertRaises(ValueError) as error:
            message = self.parking.create_parking_lot('a')
        msg = str(error.exception)
        expected_msg = "invalid literal for int() with base 10: 'a'"
        self.assertEqual(msg, expected_msg)

    def test_park(self):
        message = self.parking.park('KA-01-HH-1236', 'Green')
        self.assertEqual(message, ResponseMessages.PARKING_LOT_NOT_CREATED.value)

        self.parking.create_parking_lot(2)

        message = self.parking.park('KA-01-HH-1234', 'White')
        self.assertEqual(message, ResponseMessages.SLOT_ALLOCATED.value.format(1))

        message = self.parking.park('KA-01-HH-1234', 'White')
        self.assertEqual(message, ErrorMessages.ALREADY_EXISTING.value.format(1))

        message = self.parking.park('KA-01-HH-1235', 'Red')
        self.assertEqual(message, ResponseMessages.SLOT_ALLOCATED.value.format(2))

        message = self.parking.park('KA-01-HH-1236', 'Green')
        self.assertEqual(message, ResponseMessages.PARKING_FULL.value)

    def test_leave(self):
        message = self.parking.leave(2)
        self.assertEqual(message, ResponseMessages.PARKING_LOT_NOT_CREATED.value)

        self.parking.create_parking_lot(2)
        self.parking.park('KA-01-HH-1234', 'White')
        self.parking.park('KA-01-HH-1235', 'Red')
        message = self.parking.leave(2)
        self.assertEqual(message, ResponseMessages.SLOT_FREE.value.format(2))

        message = self.parking.leave(2)
        self.assertEqual(message, ResponseMessages.SLOT_NOT_OCCUPIED.value)

        message = self.parking.leave(3)
        self.assertEqual(message, ErrorMessages.SLOT_OUTOFRANGE.value)

        message = self.parking.leave(1)
        self.assertEqual(message, ResponseMessages.SLOT_FREE.value.format(1))
