from core.summary import Summary
from problem2.processor import Processor


def main():
    processor = Processor()
    # Print the output once before starting
    processor.print_results()
    Summary.print_message('\nEnter the kingdoms competing to be the ruler:')

    # Takes user input for competing kingdoms
    user_input = input('Input: ')
    if user_input:
        kingdom_names = processor.parse_input(user_input)
        isvalid, message = processor.validate(kingdom_names)
        if not isvalid:
            Summary.print_error(message)
            exit()

        counter = 1
        while kingdom_names:
            processor.set_competing_kingdoms(kingdom_names)
            processor.cast_vote()
            processor.process_votes()
            results = processor.get_results()
            kingdom_names = processor.check_for_tie(results)
            Summary.print_voting_result(results, counter)
            if len(kingdom_names) > 1:
                counter += 1
            else:
                break

    processor.print_results()


if __name__ == '__main__':
    main()
