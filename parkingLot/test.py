import unittest
import parking_lot


class TestParkMethods(unittest.TestCase):
    '''
    - Since methods needs to be sequential, combination of different
      methods added under single test case
    '''

    def setUp(self):
        self.park = parking_lot.Park()

    def test_interactive_input1(self):
        params = ['create_parking_lot', '3']
        self.assertEqual(self.park.trigger_action(params), 'Created a parking lot with 3 slots')

        params = ['park', 'KA-01-HH-1234', 'White']
        self.assertEqual(self.park.trigger_action(params), 'Allocated slot number: 1')
        params = ['park', 'KA-01-HH-9999', 'White']
        self.assertEqual(self.park.trigger_action(params), 'Allocated slot number: 2')
        params = ['park', 'KA-01-HH-7777', 'Red']
        self.assertEqual(self.park.trigger_action(params), 'Allocated slot number: 3')

        params = ['leave', '3']
        self.assertEqual(self.park.trigger_action(params), 'Slot number 3 is free')
        params = ['leave', '4']
        self.assertEqual(self.park.trigger_action(params), '4 Slot is not available')

        params = ['registration_numbers_for_cars_with_colour', 'White']
        self.assertEqual(self.park.trigger_action(params), 'KA-01-HH-1234, KA-01-HH-9999')

        params = ['slot_numbers_for_cars_with_colour', 'White']
        self.assertEqual(self.park.trigger_action(params), '1, 2')

        params = ['slot_number_for_registration_number', 'KA-01-HH-1234']
        self.assertEqual(self.park.trigger_action(params), '1')

    def test_interactive_input2(self):
        self.park = parking_lot.Park()
        params = ['park', 'KA-01-HH-1234', 'White']
        self.assertEqual(self.park.trigger_action(params),
                         'Sorry Parking lot not created. Please create the lot before parking the car')

        params = ['create_parking_lot', '2']
        self.assertEqual(self.park.trigger_action(params), 'Created a parking lot with 2 slots')

        params = ['park', 'KA-01-HH-1234', 'White']
        self.assertEqual(self.park.trigger_action(params), 'Allocated slot number: 1')
        params = ['park', 'KA-01-HH-9999', 'White']
        self.assertEqual(self.park.trigger_action(params), 'Allocated slot number: 2')
        params = ['park', 'KA-01-HH-7777', 'Red']
        self.assertEqual(self.park.trigger_action(params), 'Sorry, parking lot is full')

        params = ['slot_number_for_registration_number', 'KA-01-HH-8888']
        self.assertEqual(self.park.trigger_action(params), 'Not found')


if __name__ == '__main__':
    unittest.main()
