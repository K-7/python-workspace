class Summary(object):
    @classmethod
    def print_message(cls, output):
        print('{0}'.format(output))

    @classmethod
    def print_error(cls, output):
        print('Error: {0}'.format(output))

    @classmethod
    def print_ruler(cls, ruler):
        print('Who is the ruler of Southeros?')
        print('Ouput: {0}'.format(ruler))

    @classmethod
    def print_allies(cls, allies):
        print('Allies of Ruler?')
        print('Output: {0}'.format(allies))

    @classmethod
    def print_voting_result(cls, output, counter):
        print('Results after round {0} ballot count'.format(counter))
        for kingdom, allies in output.items():
            print('Output: Allies for {0} : {1}'.format(kingdom.capitalize(), len(allies)))
