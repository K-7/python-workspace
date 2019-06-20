from core.summary import Summary
from problem1.processor import Processor


def main():
    processor = Processor()
    user_input = True
    # Print the output once before starting
    processor.print_results()
    Summary.print_message('\nInput Messages to kingdoms from King Shan:')
    while user_input:
        user_input = input('Input: ')
        # If no input given by user then break
        if user_input:
            # Parse & vlidate the input
            name, message_txt = processor.parse_input(user_input)
            isvalid, message = processor.validate(name, message_txt)
            # Caste the vote to vote ballot
            if isvalid:
                processor.cast_vote(name, message_txt)
            else:
                Summary.print_error(message)
        else:
            # Once casting of vote is stopped, process & print the results
            user_input = False
            processor.process_votes()
            processor.print_results()


if __name__ == '__main__':
    main()
