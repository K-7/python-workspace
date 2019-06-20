from parking_app.constants import ErrorMessages
from parking_app.constants import UserAction
from parking_app.parking_lot import ParkingLot
from parking_app.search_parking import SearchParking
from abc import ABC, abstractmethod


class BaseProcessor(ABC):
    @abstractmethod
    def parse_input(self, string_message):
        pass

    @abstractmethod
    def validate(self, action, input_list):
        pass

    @abstractmethod
    def execute(self, action, input_list):
        pass


class Processor(BaseProcessor):

    def __init__(self):
        self.parking = ParkingLot()
        self.search_parking = SearchParking(
            parking=self.parking
        )

    def parse_input(self, string_message):
        params = string_message.split(' ')
        return params[0], params[1:]

    def validate(self, action, input_list):

        if action == UserAction.CREATE_PARKING_LOT.value:
            if not len(input_list) == 1:
                return False, ErrorMessages.INVALID_INPUT.value
            # Check whether the input is an integer
            try:
                n = int(input_list[0])
            except ValueError:
                return False, ErrorMessages.INVALID_INPUT.value
            return True, None

        elif action == UserAction.PARK.value:
            # check whether 2 input exists
            if not len(input_list) == 2:
                return False, ErrorMessages.INVALID_INPUT.value
            return True, None

        elif action == UserAction.LEAVE.value:
            if not len(input_list) == 1:
                return False, ErrorMessages.INVALID_INPUT.value
            # Check whether the input is an integer
            try:
                n = int(input_list[0])
            except ValueError:
                return False, ErrorMessages.INVALID_INPUT.value
            return True, None

        elif action == UserAction.REGISTRATION_NUMBERS_FOR_CARS_WITH_COLOUR.value:
            if not len(input_list) == 1:
                return False, ErrorMessages.INVALID_INPUT.value
            return True, None

        elif action == UserAction.SLOT_NUMBERS_FOR_CARS_WITH_COLOUR.value:
            if not len(input_list) == 1:
                return False, ErrorMessages.INVALID_INPUT.value
            return True, None

        elif action == UserAction.SLOT_NUMBER_FOR_REGISTRATION_NUMBER.value:
            if not len(input_list) == 1:
                return False, ErrorMessages.INVALID_INPUT.value
            return True, None

        elif action == UserAction.EXIT.value:
            return True, None

        elif action == UserAction.STATUS.value:
            return True, None

        else:
            return False, ErrorMessages.INVALID_ACTION.value

    def execute(self, action, input_list):
        if action == UserAction.CREATE_PARKING_LOT.value:
            return self.parking.create_parking_lot(input_list[0])

        elif action == UserAction.PARK.value:
            return self.parking.park(input_list[0], input_list[1])

        elif action == UserAction.LEAVE.value:
            return self.parking.leave(input_list[0])

        elif action == UserAction.STATUS.value:
            return self.search_parking.status()

        elif action == UserAction.REGISTRATION_NUMBERS_FOR_CARS_WITH_COLOUR.value:
            return self.search_parking.registration_numbers_for_cars_with_colour(input_list[0])

        elif action == UserAction.SLOT_NUMBERS_FOR_CARS_WITH_COLOUR.value:
            return self.search_parking.slot_numbers_for_cars_with_colour(input_list[0])

        elif action == UserAction.SLOT_NUMBER_FOR_REGISTRATION_NUMBER.value:
            return self.search_parking.slot_number_for_registration_number(input_list[0])

        elif action == UserAction.EXIT.value:
            return action
