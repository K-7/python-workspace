from core.constants import ErrorMessages
from core.constants import KINGDOMS
from core.summary import Summary
from core.vote_generator import VoteGenerator
from core.voting_machine import VotingMachine


class Processor(object):

    def __init__(self):
        self.voting_machine = VotingMachine()
        self.competing_kingdoms = {}
        self.vote_ballot = []

    def parse_input(self, string_message):
        """
        :param string_message:
        :Convert kingdom names to lowercase
        :return: Tokenised input
        """
        return [name.lower() for name in string_message.split(' ')]

    def validate(self, name_list):
        """
        :param name_list: List of Kingdom names as String
        Checks whether user input is valid or not
        """
        for name in name_list:
            # If unknown kingdom
            if name not in KINGDOMS.keys():
                return False, ErrorMessages.INVALID_KINGDOM.value.format(name)

            # If multiple messages is sent to same kingdom (Duplicate message)
            if name in self.competing_kingdoms.keys():
                return False, ErrorMessages.DUPLICATE_MESSAGE.value
            else:
                self.competing_kingdoms[name] = []

        return True, None

    def set_competing_kingdoms(self, kingdom_list):
        """
        Reset the competing_kingdom list
        :param kingdom_list: New list of kingdoms participating in ballot
        """
        self.vote_ballot = []
        if kingdom_list:
            self.competing_kingdoms = {}
            for name in kingdom_list:
                self.competing_kingdoms[name] = []

    def cast_vote(self):
        """
        Using Generator create message object and add them to vote ballot
        """
        vote_generator = VoteGenerator(self.competing_kingdoms)
        self.vote_ballot = vote_generator.execute()

    def process_votes(self):
        self.voting_machine.execute(self.vote_ballot, self.competing_kingdoms)

    def print_results(self):
        ruler, allies = self.voting_machine.get_ruler_and_allies()
        Summary.print_ruler(ruler)
        Summary.print_allies(allies)

    def get_results(self):
        return self.voting_machine.results()

    def check_for_tie(self, results):
        # Return all kingdom names who have a tie
        kingdom_dict = self.voting_machine.check_for_tie(results)
        return list(kingdom_dict.keys())
