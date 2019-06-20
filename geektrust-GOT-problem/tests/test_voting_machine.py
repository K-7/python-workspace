"""
Test voting machine and Vote generator
"""
import unittest

from core.models import Kingdom
from core.models import Message
from core.vote_generator import VoteGenerator
from core.voting_machine import VotingMachine


class TestVotingMachine(unittest.TestCase):
    def setUp(self):
        self.competing_kingdoms = {
            'air': [],
            'land': []
        }
        vote_generator = VoteGenerator(self.competing_kingdoms)
        self.vote_ballot = vote_generator.execute()

    def test_vote_generator(self):
        """
        Check whether vote generator generates 6 votes
        """
        self.assertEqual(len(self.vote_ballot), 6)

    def test_voting_machine(self):
        voting_machine = VotingMachine()
        voting_machine.execute(self.vote_ballot, self.competing_kingdoms)
        results = voting_machine.results()
        self.assertEqual(len(results.keys()), len(self.competing_kingdoms.keys()))

    def test_kingdom_result(self):
        """
        Unit test case for kingdom_result method. Used in Problem1
        """
        voting_machine = VotingMachine()
        vote_ballot = []
        all_kingdoms = ['land', 'air', 'ice']
        competing_kingdoms = {'space': []}
        for name in all_kingdoms:
            sender = Kingdom.get_kingdom('space')
            receiver = Kingdom.get_kingdom(name)
            message_txt = 'oaaawaalaa1d22n333a4444pzmzmzmzaztzozh'
            message_obj = Message(sender, receiver, message_txt)
            vote_ballot.append(message_obj)

        voting_machine.execute(vote_ballot, competing_kingdoms)
        ruler, allies = voting_machine.kingdom_result('space', 2)
        self.assertEqual(ruler, 'Space')
        self.assertEqual(allies, 'Land, Air, Ice')
