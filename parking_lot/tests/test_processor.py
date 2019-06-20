from parking_app.constants import ResponseMessages
from tests.test_base import TestBase
from parking_app.constants import ErrorMessages


class TestProcessor(TestBase):

    def test_parse_input(self):
        action, inputs = self.processor.parse_input('park KA-01-HH-9999 White')
        self.assertEqual(action, 'park')
        self.assertEqual(inputs, ['KA-01-HH-9999', 'White'])

        action, inputs = self.processor.parse_input('create_parking_lot')
        self.assertEqual(action, 'create_parking_lot')
        self.assertEqual(inputs, [])

        action, inputs = self.processor.parse_input('')
        self.assertEqual(action, '')
        self.assertEqual(inputs, [])

        action, inputs = self.processor.parse_input('status')
        self.assertEqual(action, 'status')
        self.assertEqual(inputs, [])

    def test_validate(self):
        action, inputs = self.processor.parse_input('park KA-01-HH-9999 White')
        isvalid, error_message = self.processor.validate(action, inputs)
        self.assertEqual(isvalid, True)
        self.assertEqual(error_message, None)

        action, inputs = self.processor.parse_input('create_parking_lot 6')
        isvalid, error_message = self.processor.validate(action, inputs)
        self.assertEqual(isvalid, True)
        self.assertEqual(error_message, None)

        action, inputs = self.processor.parse_input('registration_numbers_for_cars_with_colour White')
        isvalid, error_message = self.processor.validate(action, inputs)
        self.assertEqual(isvalid, True)
        self.assertEqual(error_message, None)

        action, inputs = self.processor.parse_input('park KA-01-HH-9999')
        isvalid, error_message = self.processor.validate(action, inputs)
        self.assertEqual(isvalid, False)
        self.assertEqual(error_message, ErrorMessages.INVALID_INPUT.value)

        action, inputs = self.processor.parse_input('create_parking_lot aa')
        isvalid, error_message = self.processor.validate(action, inputs)
        self.assertEqual(isvalid, False)
        self.assertEqual(error_message, ErrorMessages.INVALID_INPUT.value)

        action, inputs = self.processor.parse_input('leave .')
        isvalid, error_message = self.processor.validate(action, inputs)
        self.assertEqual(isvalid, False)
        self.assertEqual(error_message, ErrorMessages.INVALID_INPUT.value)

    def test_execute(self):
        action, inputs = self.processor.parse_input('create_parking_lot 3')
        message = self.processor.execute(action, inputs)
        self.assertEqual(message, ResponseMessages.PARKING_LOT_CREATED.value.format(3))

        action, inputs = self.processor.parse_input('park KA-01-HH-9999 White')
        message = self.processor.execute(action, inputs)
        self.assertEqual(message, ResponseMessages.SLOT_ALLOCATED.value.format(1))

        action, inputs = self.processor.parse_input('park KA-01-HH-9997 White')
        message = self.processor.execute(action, inputs)
        self.assertEqual(message, ResponseMessages.SLOT_ALLOCATED.value.format(2))

        action, inputs = self.processor.parse_input('park KA-01-HH-9994 Red')
        message = self.processor.execute(action, inputs)
        self.assertEqual(message, ResponseMessages.SLOT_ALLOCATED.value.format(3))

        action, inputs = self.processor.parse_input('registration_numbers_for_cars_with_colour White')
        message = self.processor.execute(action, inputs)
        self.assertEqual(message, 'KA-01-HH-9999, KA-01-HH-9997')

        action, inputs = self.processor.parse_input('slot_numbers_for_cars_with_colour White')
        message = self.processor.execute(action, inputs)
        self.assertEqual(message, '1, 2')

        action, inputs = self.processor.parse_input('slot_number_for_registration_number KA-01-HH-9994')
        message = self.processor.execute(action, inputs)
        self.assertEqual(message, '3')
