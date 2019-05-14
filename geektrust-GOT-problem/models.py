"""
All the common Classes & functions are declared in this file
"""
import random
from collections import Counter
from abc import ABC, abstractmethod


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

    @property
    def display_name(self):
        return self.name.capitalize()


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
    and picks a random message
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
        with open('messages.txt', 'r') as f:
            for line in f:
                self.message_list.append(line.strip())

    def get_message(self):
        # Get random message from the List
        return random.choice(self.message_list)


class BaseProcessor(ABC):
    def __init__(self):
        self.ruler = None
        self.allies = []
        self.kingdoms = {
            'land': 'panda',
            'water': 'octopus',
            'ice': 'mammoth',
            'air': 'owl',
            'fire': 'dragon',
            'space': 'gorilla'
        }

    def get_kingdom(self, name):
        if name.lower() not in self.kingdoms.keys():
            raise ValueError('Invalid kingdom name')

        return Kingdom(
            name=name.lower(),
            emblem=self.kingdoms[name.lower()],
            ruler=False
        )

    def get_random_kingdom(self, excluded_name=None):
        # Get random Kingdom from the available list
        name = None
        while name == excluded_name or name is None:
            name = random.choice(self.kingdoms.keys())
        return self.get_kingdom(name)

    def get_message_obj(self, sender, receiver, message):
        return Message(
            sender=sender,
            receiver=receiver,
            message=message
        )

    @abstractmethod
    def process_input(self):
        pass

    def print_output(self, output):
        if output != -1:
            if type(output) == Kingdom:
                print('Output: {0}'.format(output.name))
            elif type(output) == list:
                output_allies = [out.display_name for out in output]
                print('Output: {0}'.format(', '.join(output_allies)))
            elif type(output) == dict:
                for kingdom, allies in output.items():
                    print('Output: Allies for {0} : {1}'.format(kingdom, len(allies)))
            else:
                print('Output: {0}'.format(output))
