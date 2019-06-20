from enum import Enum


class UserAction(Enum):
    CREATE_PARKING_LOT = 'create_parking_lot'
    PARK = 'park'
    LEAVE = 'leave'
    STATUS = 'status'
    REGISTRATION_NUMBERS_FOR_CARS_WITH_COLOUR = 'registration_numbers_for_cars_with_colour'
    SLOT_NUMBERS_FOR_CARS_WITH_COLOUR = 'slot_numbers_for_cars_with_colour'
    SLOT_NUMBER_FOR_REGISTRATION_NUMBER = 'slot_number_for_registration_number'
    EXIT = 'exit'


class ErrorMessages(Enum):
    SLOT_OUTOFRANGE = 'ERROR: {0} Slot no. is not available in the slots'
    INVALID_INPUT = 'ERROR: Invalid Input'
    INVALID_ACTION = 'ERROR: Invalid Action'
    ALREADY_EXISTING = 'ERROR: Car with this Registration no. is already parked'


class ResponseMessages(Enum):
    NOT_FOUND = 'Not found'
    PARKING_FULL = 'Sorry, parking lot is full'
    PARKING_LOT_CREATED = 'Created a parking lot with {0} slots'
    SLOT_ALLOCATED = 'Allocated slot number: {0}'
    SLOT_FREE = 'Slot number {0} is free'
    PARKING_LOT_NOT_CREATED = 'Sorry Parking lot not available'
    SLOT_NOT_OCCUPIED = '{0} Slot is not occupied'
    STATUS_HEADERS = 'Slot No.  Registration No   Colour'


class ParkingAction(Enum):
    PARK = 'park'
    REMOVE = 'remove'
