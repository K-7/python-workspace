#! /usr/bin/python -tt
import sys


class CarDetail(object):
    def __init__(self, reg_no, colour, slot):
        self.reg_no = reg_no
        self.colour = colour
        self.slot = slot

    def __str__(self):
        return '{0}         {1}     {2}'.format(self.slot, self.reg_no, self.colour)


class Park(object):
    def __init__(self):
        self.action = None
        self.option1 = None
        self.option2 = None
        self.parking_slots = []
        self.max_slot_no = 0

    def trigger_action(self, params):
        '''
        :param params: Consists of Input action and other options as a list of maximum length 3
        :return: String is returned back
        '''
        self.action = params[0].strip()
        self.option1 = params[1].strip() if len(params) > 1 else None
        self.option2 = params[2].strip() if len(params) > 2 else None

        if self.action == 'create_parking_lot':
            return self.create_parking_lot(self.option1)
        elif self.action == 'park':
            return self.park(self.option1, self.option2)
        elif self.action == 'leave':
            return self.leave(self.option1)
        elif self.action == 'status':
            return self.status()
        elif self.action == 'registration_numbers_for_cars_with_colour':
            return self.registration_numbers_for_cars_with_colour(self.option1)
        elif self.action == 'slot_numbers_for_cars_with_colour':
            return self.slot_numbers_for_cars_with_colour(self.option1)
        elif self.action == 'slot_number_for_registration_number':
            return self.slot_number_for_registration_number(self.option1)
        elif self.action == 'exit':
            return self.action
        else:
            return 'Inappropriate Action !!'

    def create_parking_lot(self, slot_no):
        self.max_slot_no = int(slot_no)
        self.parking_slots = [None for i in range(0, self.max_slot_no)]
        return 'Created a parking lot with {0} slots'.format(slot_no)

    def park(self, reg_no, colour):
        parking_lost_full = True
        if len(self.parking_slots) < 1:
            return 'Sorry Parking lot not created. Please create the lot before parking the car'
        for index, slot in enumerate(self.parking_slots):
            if not slot:
                parking_lost_full = False
                self.parking_slots[index] = CarDetail(reg_no, colour, index + 1)
                return 'Allocated slot number: {0}'.format(index + 1)

        if parking_lost_full == True:
            return 'Sorry, parking lot is full'

    def leave(self, slot_no):
        slot_no = int(slot_no)
        if slot_no <= len(self.parking_slots):
            self.parking_slots[slot_no - 1] = None
            return 'Slot number {0} is free'.format(slot_no)
        else:
            return '{0} Slot is not available'.format(slot_no)

    def status(self):
        markup = 'Slot No.  Registration No   Colour'
        for slot in self.parking_slots:
            if slot:
                markup += '\n' + str(slot)
        return markup

    def registration_numbers_for_cars_with_colour(self, colour):
        reg_no_list = []
        for slot in self.parking_slots:
            if slot and slot.colour == colour:
                reg_no_list.append(slot.reg_no)

        return ', '.join(reg_no_list)

    def slot_numbers_for_cars_with_colour(self, colour):
        slot_list = []
        for slot in self.parking_slots:
            if slot and slot.colour == colour:
                slot_list.append(str(slot.slot))

        return ', '.join(slot_list)

    def slot_number_for_registration_number(self, reg_no):
        slot_no = None
        for slot in self.parking_slots:
            if slot and slot.reg_no == reg_no:
                slot_no = slot.slot
        if slot_no:
            return str(slot_no)
        else:
            return 'Not found'


def main():
    '''Main function checks whether file is specified as argument
       and decides whether Input is Interactive or read from the file
    '''
    file_name = sys.argv[1] if len(sys.argv) > 1 else None
    park = Park()
    if file_name:
        f = open(file_name, 'r')
        print '---------Input (contents of file)---------'
        for line in f:
            print line.strip()
        print '---------Output (to STDOUT)---------'
        f.seek(0)
        for line in f:
            params = line.split(' ')
            print park.trigger_action(params)
    else:
        action = True
        while action:
            print 'Input:'
            params = raw_input().split(' ')
            print 'Output'
            result = park.trigger_action(params)
            if result == 'exit':
                action = False
            else:
                print result


if __name__ == '__main__':
    main()
