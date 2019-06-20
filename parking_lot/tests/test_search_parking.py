from parking_app.constants import ResponseMessages
from tests.test_base import TestBase


class TestSearchParking(TestBase):

    def test_status(self):
        self.parking.create_parking_lot(2)
        self.parking.park('KA-01-HH-1234', 'White')
        message = self.search_parking.status()
        expected_msg = ResponseMessages.STATUS_HEADERS.value
        for slot in self.parking.get_parking_lot:
            if slot:
                expected_msg += '\n' + str(slot)
        self.assertEqual(message, expected_msg)

    def test_registration_numbers_for_cars_with_colour(self):
        self.parking.create_parking_lot(3)
        self.parking.park('KA-01-HH-1234', 'White')
        self.parking.park('KA-01-HH-1235', 'Red')
        self.parking.park('KA-01-HH-1236', 'White')
        message = self.search_parking.registration_numbers_for_cars_with_colour('White')
        self.assertEqual(message, 'KA-01-HH-1234, KA-01-HH-1236')
        self.parking.create_parking_lot(2)
        self.parking.park('KA-01-HH-1234', 'White')
        self.parking.park('KA-01-HH-1235', 'Red')
        self.parking.park('KA-01-HH-1236', 'White')
        message = self.search_parking.registration_numbers_for_cars_with_colour('White')
        self.assertEqual(message, 'KA-01-HH-1234')
        message = self.search_parking.slot_numbers_for_cars_with_colour('Orange')
        self.assertEqual(message, ResponseMessages.NOT_FOUND.value)

    def test_slot_numbers_for_cars_with_colour(self):
        self.parking.create_parking_lot(3)
        self.parking.park('KA-01-HH-1234', 'White')
        self.parking.park('KA-01-HH-1235', 'Red')
        self.parking.park('KA-01-HH-1236', 'White')
        message = self.search_parking.slot_numbers_for_cars_with_colour('White')
        self.assertEqual(message, '1, 3')
        self.parking.create_parking_lot(2)
        self.parking.park('KA-01-HH-1234', 'White')
        self.parking.park('KA-01-HH-1235', 'Red')
        self.parking.park('KA-01-HH-1236', 'White')
        message = self.search_parking.slot_numbers_for_cars_with_colour('White')
        self.assertEqual(message, '1')
        message = self.search_parking.slot_numbers_for_cars_with_colour('Orange')
        self.assertEqual(message, ResponseMessages.NOT_FOUND.value)

    def test_slot_number_for_registration_number(self):
        self.parking.create_parking_lot(3)
        self.parking.park('KA-01-HH-1234', 'White')
        self.parking.park('KA-01-HH-1235', 'Red')
        self.parking.park('KA-01-HH-1236', 'White')
        message = self.search_parking.slot_number_for_registration_number('KA-01-HH-1236')
        self.assertEqual(message, '3')
        self.parking.create_parking_lot(2)
        self.parking.park('KA-01-HH-1234', 'White')
        self.parking.park('KA-01-HH-1235', 'Red')
        self.parking.park('KA-01-HH-1236', 'White')
        message = self.search_parking.slot_number_for_registration_number('KA-01-HH-1236')
        self.assertEqual(message, ResponseMessages.NOT_FOUND.value)
        message = self.search_parking.slot_number_for_registration_number('KA-01-HH-1237')
        self.assertEqual(message, ResponseMessages.NOT_FOUND.value)
