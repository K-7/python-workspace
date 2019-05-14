import models
import random


class Processor(models.BaseProcessor):
    def __init__(self):
        self.competing_kingdoms = {}
        self.vote_ballot = []
        self.selected_votes = []
        super().__init__()

    def __get_message_txt(self):
        # Get random message from MessageTable
        message_table = models.MessageTable()
        return message_table.get_message()

    def __cast_votes(self):
        # competing_kingdoms will all send messages to other kingdoms
        for ckingdom_name in self.competing_kingdoms.keys():
            for kingdom_name in self.kingdoms.keys():
                if kingdom_name != ckingdom_name:
                    sender = self.get_kingdom(ckingdom_name)
                    receiver = self.get_kingdom(kingdom_name)
                    message_txt = self.__get_message_txt()
                    message_obj = self.get_message_obj(sender, receiver, message_txt)
                    self.vote_ballot.append(message_obj)

    def __pick_six_votes(self):
        # High Priest picks 6 votes
        for i in range(1, 7):
            self.selected_votes.append(
                random.choice(self.vote_ballot)
            )

    def __is_valid_vote(self, sender, receiver):
        # check whether sender is under competing_kingdoms list
        if sender.name not in self.competing_kingdoms.keys():
            return False
        # check whether receiver's vote is already present
        if receiver.name in self.competing_kingdoms[sender.name]:
            return False
        # Check whether receiving kingdom is competing to be the ruler
        if receiver.name in self.competing_kingdoms.keys():
            return False
        return True

    def __process_selected_votes(self):
        # Check whether selected votes are adding allegiance
        for vote in self.selected_votes:
            if vote.did_message_map_emblem() and self.__is_valid_vote(vote.sender, vote.receiver):
                self.competing_kingdoms[vote.sender.name].append(vote.receiver.name)

    def check_for_tie(self, c_kingdoms):
        max_vote_count = 0
        max_vote_kingdoms = {}

        # Get Maximum vote count
        for val in c_kingdoms.values():
            if len(val) > max_vote_count:
                max_vote_count = len(val)

        # Assign all tied kingdoms to a new dictionary
        for key, val in c_kingdoms.items():
            if len(val) == max_vote_count:
                max_vote_kingdoms[key] = val

        # If there is tie then change c_kingdoms
        mv_kingdom_names = list(max_vote_kingdoms.keys())

        if len(mv_kingdom_names) > 1:
            # If tie exists return those kingdom_names for repeated ballot process
            return ' '.join(mv_kingdom_names)
        elif len(mv_kingdom_names) == 1:
            # If no tie then set the ruler
            self.ruler = self.get_kingdom(mv_kingdom_names[0])
            for ally in max_vote_kingdoms[mv_kingdom_names[0]]:
                self.allies.append(self.get_kingdom(ally))
            return False

        return False

    def __process_voting(self):
        self.__cast_votes()
        self.__pick_six_votes()
        self.__process_selected_votes()

    def __reset_data(self):
        self.competing_kingdoms = {}
        self.vote_ballot = []
        self.selected_votes = []

    def __is_valid_input(self, input):
        # Check whether user entered Kingdom names are valid
        if not input:
            return False
        for kingdom_name in input.split(' '):
            if kingdom_name.lower() not in self.kingdoms.keys():
                return False
        return True

    def process_input(self, input):
        self.__reset_data()
        if input == 'Who is the ruler of Southeros?':
            return self.ruler
        elif input == 'Allies of Ruler?':
            return self.allies or None
        else:
            if not self.__is_valid_input(input):
                return '{0} : Invalid Input given'.format(input)

            for kingdom_name in input.split(' '):
                self.competing_kingdoms[kingdom_name.lower()] = []

            self.__process_voting()
            return self.competing_kingdoms


def main():
    output = None
    processor = Processor()
    while True:
        print('Who is the ruler of Southeros?')
        output = processor.process_input('Who is the ruler of Southeros?')
        processor.print_output(output)
        print('Allies of Ruler?')
        output = processor.process_input('Allies of Ruler?')
        processor.print_output(output)
        print('Enter the kingdoms competing to be the ruler:')
        user_input = input('Input: ')
        if user_input:
            tied_kingdoms = user_input
            counter = 1
            while tied_kingdoms:
                output = processor.process_input(tied_kingdoms)
                tied_kingdoms = processor.check_for_tie(output)
                print('Results after round {0} ballot count'.format(counter))
                processor.print_output(output)
                counter += 1


if __name__ == '__main__':
    main()
