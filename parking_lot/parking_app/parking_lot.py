from parking_app.car import Car
from parking_app.constants import ErrorMessages
from parking_app.constants import ParkingAction
from parking_app.constants import ResponseMessages


class ParkingLot(object):
    def __init__(self):
        self.__parking_lot = []
        self.__reg_index = {}
        self.__colour_index = {}
        self.__max_slot_size = 0

    @property
    def get_parking_lot(self):
        return self.__parking_lot

    @property
    def get_reg_index(self):
        return self.__reg_index

    @property
    def get_colour_index(self):
        return self.__colour_index

    @property
    def get_max_slot_size(self):
        return self.__max_slot_size

    def _is_slots_created(self):
        # Check whether slots are issued in the Parking lot
        return 0 < len(self.__parking_lot)

    def __is_slot_occupied(self, index):
        # check whether a given slot is occupied
        if self.__parking_lot[index] is not None:
            return True
        return False

    def __is_slot_outofrange(self, slot_no):
        # check whether slot no is greater than the max size
        if slot_no > self.__max_slot_size or self.__max_slot_size < 1:
            return True
        return False

    def __get_number(self, str_no):
        # Convert string to int
        return int(str_no)

    def __validate_before_parking(self, reg_no):
        # Check whether parking lot is created
        if not self._is_slots_created():
            return ResponseMessages.PARKING_LOT_NOT_CREATED.value

        # If the user inputs same registration no. twice
        if reg_no in self.__reg_index.keys():
            return ErrorMessages.ALREADY_EXISTING.value
        return None

    def __validate_before_leaving(self, slot_no):
        # Check whether parking lot is created
        if not self._is_slots_created():
            return ResponseMessages.PARKING_LOT_NOT_CREATED.value

        # check whether the slot_no is out of range
        if self.__is_slot_outofrange(slot_no):
            return ErrorMessages.SLOT_OUTOFRANGE.value

        # check whether the slot is occupied or empty
        if not self.__is_slot_occupied(slot_no - 1):
            return ResponseMessages.SLOT_NOT_OCCUPIED.value
        return None

    def __update_reg_index(self, reg_no, action, index):
        # Keep an index for registration no. for faster lookup

        if action == ParkingAction.PARK:
            self.__reg_index[reg_no] = index

        elif action == ParkingAction.REMOVE:
            del self.__reg_index[reg_no]

    def __update_colour_index(self, colour, action, index):
        # Keep an index for colours for faster lookup

        if action == ParkingAction.PARK:
            if colour not in self.__colour_index.keys():
                self.__colour_index[colour] = []
            self.__colour_index[colour].append(index)

        elif action == ParkingAction.REMOVE:
            self.__colour_index[colour].remove(index)
            if len(self.__colour_index[colour]) == 0:
                del self.__colour_index[colour]

    def __reset_parking(self):
        self.__parking_lot = []
        self.__reg_index = {}
        self.__colour_index = {}
        self.__max_slot_size = 0

    def create_parking_lot(self, slot_size):
        """
        Initialize all the slots with None
        :param slot_size: total no. of slots for the parking lot
        """
        self.__reset_parking()
        self.__max_slot_size = self.__get_number(slot_size)
        self.__parking_lot = [None for i in range(0, self.__max_slot_size)]
        return ResponseMessages.PARKING_LOT_CREATED.value.format(slot_size)

    def park(self, reg_no, colour):
        """
        Its assumed that the first empty position will be
        occupied by the car.
        Update index for reg_no and colors
        :param reg_no: registration no of the car
        :param colour: colour of the car
        :return: Success or failure message for a parking
        """
        error = self.__validate_before_parking(reg_no)
        if error:
            return error

        parked = False
        for index, slot in enumerate(self.__parking_lot):
            # If slot is empty
            if not slot:
                parked = True
                colour = colour.lower()
                self.__parking_lot[index] = Car(
                    reg_no=reg_no,
                    colour=colour,
                    slot_no=index + 1
                )
                self.__update_reg_index(
                    reg_no=reg_no,
                    action=ParkingAction.PARK,
                    index=index
                )
                self.__update_colour_index(
                    colour=colour,
                    action=ParkingAction.PARK,
                    index=index
                )
                return ResponseMessages.SLOT_ALLOCATED.value.format(index + 1)

        if not parked:
            return ResponseMessages.PARKING_FULL.value

    def leave(self, slot_no):
        """
        Validate the slot_no in the parking_lot
        Update index for reg_no and colors
        :param slot_no:
        :return:
        """
        slot_no = self.__get_number(slot_no)
        error = self.__validate_before_leaving(slot_no)
        if error:
            return error

        car = self.__parking_lot[slot_no - 1]
        # Set the slot empty
        self.__parking_lot[slot_no - 1] = None
        # Update the index
        self.__update_reg_index(
            reg_no=car.get_reg_no,
            action=ParkingAction.REMOVE,
            index=slot_no - 1
        )
        self.__update_colour_index(
            colour=car.get_colour_lowercase,
            action=ParkingAction.REMOVE,
            index=slot_no - 1
        )

        return ResponseMessages.SLOT_FREE.value.format(slot_no)
