from parking_app.constants import ResponseMessages


class SearchParking(object):
    def __init__(self, parking):
        self.parking = parking

    def status(self):
        """
        :return: Collection of car details in a tabular fashion
        """
        markup = ResponseMessages.STATUS_HEADERS.value
        for slot in self.parking.get_parking_lot:
            if slot:
                markup += '\n' + str(slot)
        return markup

    def registration_numbers_for_cars_with_colour(self, colour):
        """
        :param colour:
        :return: Search for the colour in the colour_index maintained
        """
        colour = colour.lower()
        if colour not in self.parking.get_colour_index.keys():
            return ResponseMessages.NOT_FOUND.value

        reg_no_list = [
            self.parking.get_parking_lot[index].get_reg_no for index in self.parking.get_colour_index[colour]
        ]
        return ', '.join(reg_no_list)

    def slot_numbers_for_cars_with_colour(self, colour):
        """
        Since indices are maintained, we need to add + 1 to give the exact position
        :param colour:
        :return: Search for the colour in the colour_index maintained
        """
        colour = colour.lower()
        if colour not in self.parking.get_colour_index.keys():
            return ResponseMessages.NOT_FOUND.value

        return ', '.join([str(i + 1) for i in self.parking.get_colour_index[colour]])

    def slot_number_for_registration_number(self, reg_no):
        """
        :param reg_no:
        :return: Search for the reg_no in the reg_index maintained
        """
        if reg_no not in self.parking.get_reg_index.keys():
            return ResponseMessages.NOT_FOUND.value

        return '{0}'.format(
            self.parking.get_reg_index[reg_no] + 1
        )
