from core.constants import ErrorMessages
from core.constants import KINGDOMS
from core.models import Kingdom
from core.models import Message
from core.summary import Summary
from core.voting_machine import VotingMachine


class Processor(object):

    def __init__(self):
        self.voting_machine = VotingMachine()
        self.vote_ballot = []
        self.competing_kingdoms = {'space': []}

    def parse_input(self, string_message):
        """
        :param string_message:
        :Convert kingdom names to lowercase
        :return: Tokenised input
        """
        try:
            name, message_txt = string_message.split(', ')
        except ValueError:
            return string_message, None
        name = name.lower()
        message_txt = message_txt.replace('"', '')
        return name, message_txt

    def validate(self, name, message_txt):
        """
        :param name: Kingdom name as String
        :param message_txt: Message to Kingdom as String
        Checks whether user input is valid or not
        """
        # If unknown kingdom
        if name not in KINGDOMS.keys():
            return False, ErrorMessages.INVALID_KINGDOM.value.format(name)

        # If message is empty
        if not message_txt:
            return False, ErrorMessages.INVALID_MESSAGE.value

        # If multiple messages is sent to same kingdom (Duplicate message)
        for message in self.vote_ballot:
            if message.receiver.name == name:
                return False, ErrorMessages.DUPLICATE_MESSAGE.value

        return True, None

    def cast_vote(self, name, message_text):
        """
        :param name: kingdom name
        :param message_text:
        Create message object and add them to vote ballot
        """
        kingdom = Kingdom.get_kingdom(name)
        ruler_kingdom = Kingdom.get_kingdom('space')
        message_obj = Message(ruler_kingdom, kingdom, message_text)
        self.vote_ballot.append(message_obj)

    def process_votes(self):
        self.voting_machine.execute(self.vote_ballot, self.competing_kingdoms)

    def print_results(self):
        ruler, allies = self.voting_machine.kingdom_result('space', 2)
        Summary.print_ruler(ruler)
        Summary.print_allies(allies)
