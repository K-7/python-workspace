class Car(object):
    def __init__(self, reg_no, colour, slot_no):
        self.__reg_no = reg_no
        self.__colour = colour
        self.__slot_no = slot_no

    def __setattr__(self, name, value):
        if value is None or value == '':
            raise TypeError('{0} cannot be empty or NULL'.format(name))
        if name == '_Car__slot_no' and not isinstance(value, int):
            raise TypeError('slot_no must be of type int')

        super().__setattr__(name, value)

    def __str__(self):
        return '{0}         {1}     {2}'.format(
            self.get_slot,
            self.get_reg_no,
            self.get_colour
        )

    @property
    def get_reg_no(self):
        return self.__reg_no

    @property
    def get_slot(self):
        return self.__slot_no

    @property
    def get_colour(self):
        return self.__colour.capitalize()

    @property
    def get_colour_lowercase(self):
        return self.__colour
