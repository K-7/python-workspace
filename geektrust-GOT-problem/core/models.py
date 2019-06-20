"""
All the common Classes & functions are declared in this file

Areas of Improvement:
The output is incorrect. If 'Air, owl' as a message is sent 3 times,
then the solution declares King Shan as the King and displays Air as an ally 3 times.
This is not correct as King Shan needs to win 3 kingdoms to rule Southeros.

All the logic is in one big method/file which makes the code hard to read and maintain.
Currently Processor in problem2.py class has too many responsibilities.
Ideally a class should have one responsibility [Single Responsibility Principle].
Try to break it down to smaller classes.

The Proccessor class has behaviours like kingdoms casting their votes,
high priest picking random votes, validation of the votes, calculation of the votes, processing input etc.
Ideally the processor should just have been an orchestrator.
Try to identify some more domain models.
And delegate some of the behaviours to the new classes and existing classes.
Currently Kingdom class has no behaviour. The secret message is sent to a Kingdom.
The kingdom should be able to tell whether the message is valid or not.

Try to keep the problem class as light as possible.
Delegate the behaviours to all the domain classes.
Tests are not really unit tests.
Ideally all public methods in the solution should be tested as individual units.

"""
import os
import random
from collections import Counter

from core.constants import KINGDOMS


class Kingdom(object):
    def __init__(self, name, emblem, ruler=False):
        self.name = name
        self.emblem = emblem
        self.ruler = ruler

    def __setattr__(self, name, value):
        if value is None or value == '':
            raise TypeError('{0} cannot be empty of NULL'.format(name))
        if name == 'ruler' and not isinstance(value, bool):
            raise TypeError('ruler must be of type bool')

        super().__setattr__(name, value)

    def __str__(self):
        return self.display_name

    @property
    def display_name(self):
        return self.name.capitalize()

    @classmethod
    def get_kingdom(cls, name):
        return Kingdom(
            name=name,
            emblem=KINGDOMS[name],
            ruler=False
        )


class Message(object):
    def __init__(self, sender, receiver, message):
        self.sender = sender
        self.receiver = receiver
        self.message = message

    def __setattr__(self, name, value):
        if not value:
            raise TypeError('{0} cannot be empty of NULL'.format(name))
        if (name == 'sender' or name == 'receiver') and not isinstance(value, Kingdom):
            raise TypeError('{0} must be of type Kingdom'.format(name))

        super().__setattr__(name, value)

    def did_message_map_emblem(self):
        emblem = Counter(self.receiver.emblem.lower())
        message = Counter(self.message.lower())
        for key in emblem.keys():
            # If emblem individual char count is greater than message individual char count
            if emblem[key] > message[key]:
                return False
        return True


class MessageTable(object):
    """
    Loads all messages from the default file location
    and picks a random message.
    This is a singleton class
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        # This class is a Singleton class
        if cls.__instance is not None:
            return cls.__instance
        else:
            cls.__instance = super().__new__(cls)
            return cls.__instance

    def __init__(self):
        self.message_list = []
        self.load_file_content()

    def load_file_content(self):
        # Read a file and load it to a List line by line
        if self.message_list:
            return
        root_path = os.path.dirname(os.path.abspath(__file__))
        with open('{0}/../data/messages.txt'.format(root_path), 'r') as f:
            for line in f:
                self.message_list.append(line.strip())

    def get_message(self):
        # Get random message from the List
        return random.choice(self.message_list)

    @classmethod
    def get_random_message(cls):
        # Get random message from MessageTable
        message_table = MessageTable()
        return message_table.get_message()
