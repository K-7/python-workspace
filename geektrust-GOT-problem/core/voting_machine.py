class VotingMachine(object):
    """
    Process the collected votes. Create dictionary of [kingdom : allies]
    """

    def __init__(self):
        self.__competing_kingdoms = {}
        self.__votes = []
        self.__max_vote_kingdoms = {}

    def get_ruler_and_allies(self):
        """
        return the first max vote kingdom
        """

        if self.__max_vote_kingdoms:
            key = list(self.__max_vote_kingdoms.keys())[0]
            ruler = key.capitalize()
            allies = ', '.join([name.capitalize() for name in self.__max_vote_kingdoms[key]])
        else:
            ruler = None
            allies = None

        return ruler, allies

    def results(self):
        return self.__competing_kingdoms

    def kingdom_result(self, name, min_count=0):
        """
        :param name: Kingdom name
        :param min_count: Minimum votes needed to become ruler
        Accepts a kingdom name and checks whether the selected kingdom
        has minimun votes to become a ruler
        """
        if name in self.__competing_kingdoms.keys() and len(self.__competing_kingdoms[name]) > min_count:
            ruler = name.capitalize()
            allies = ', '.join([name.capitalize() for name in self.__competing_kingdoms[name]])
        else:
            ruler = None
            allies = None
        return ruler, allies

    def __is_valid_vote(self, sender, receiver):
        # check whether sender is under competing_kingdoms list
        if sender.name not in self.__competing_kingdoms.keys():
            return False
        # check whether receiver's vote is already present
        if receiver.name in self.__competing_kingdoms[sender.name]:
            return False
        # Check whether receiving kingdom is competing to be the ruler
        if receiver.name in self.__competing_kingdoms.keys():
            return False
        return True

    def __process_votes(self):
        # Check whether votes in ballot are adding alliance
        for vote in self.__votes:
            if vote.did_message_map_emblem() and self.__is_valid_vote(vote.sender, vote.receiver):
                self.__competing_kingdoms[vote.sender.name].append(vote.receiver.name)

    def execute(self, vote_ballot, competing_kingdoms):
        self.__competing_kingdoms = competing_kingdoms
        self.__votes = vote_ballot
        self.__process_votes()

    def check_for_tie(self, kingdoms):
        max_vote_count = 0
        self.__max_vote_kingdoms = {}

        # Get Maximum vote count
        for val in kingdoms.values():
            if len(val) > max_vote_count:
                max_vote_count = len(val)

        # Assign all tied kingdoms to a new dictionary
        for key, val in kingdoms.items():
            if len(val) == max_vote_count:
                self.__max_vote_kingdoms[key] = val

        return self.__max_vote_kingdoms
