import random

from core.constants import KINGDOMS
from core.models import Kingdom
from core.models import Message
from core.models import MessageTable


class VoteGenerator(object):
    """
    Create random message objects using MessageTable.
    Mimic competing_kingdoms sending messages to all other Kingdoms
    Out of all the messages, pick 6 random messages
    """

    def __init__(self, competing_kingdoms):
        self.vote_ballot = []
        self.selected_votes = []
        self.competing_kingdoms = competing_kingdoms

    def __cast_votes(self):
        # competing_kingdoms will all send messages to other kingdoms
        for ckingdom_name in self.competing_kingdoms.keys():
            for kingdom_name in KINGDOMS.keys():
                if kingdom_name != ckingdom_name:
                    sender = Kingdom.get_kingdom(ckingdom_name)
                    receiver = Kingdom.get_kingdom(kingdom_name)
                    message_txt = MessageTable.get_random_message()
                    message_obj = Message(sender, receiver, message_txt)
                    self.vote_ballot.append(message_obj)

    def __pick_six_votes(self):
        # High Priest picks 6 votes
        for i in range(1, 7):
            self.selected_votes.append(
                random.choice(self.vote_ballot)
            )

    def execute(self):
        self.__cast_votes()
        self.__pick_six_votes()
        return self.selected_votes
