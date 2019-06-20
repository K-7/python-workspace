import sys
from parking_app.processor import Processor


def main():
    '''Main function checks whether file is specified as argument
       and decides whether Input is Interactive or read from the file
    '''
    file_name = sys.argv[1] if len(sys.argv) > 1 else None
    processor = Processor()
    if file_name:
        f = open(file_name, 'r')
        print('---------Input (contents of file)---------')
        for line in f:
            print(line.strip())
        print('---------Output (to STDOUT)---------')
        f.seek(0)
        for line in f:
            # When read from file new line characters are present
            new_line = line.replace('\n', '')
            action, inputs = processor.parse_input(new_line)
            isvalid, error_message = processor.validate(action, inputs)
            # If valid execute the input
            if isvalid:
                print(processor.execute(action, inputs))
            else:
                print(error_message)
    else:
        action = True
        while action:
            print('Input:')
            user_input = input()
            action, inputs = processor.parse_input(user_input)
            print('Output:')
            isvalid, error_message = processor.validate(action, inputs)
            # If valid execute the input
            if isvalid:
                result = processor.execute(action, inputs)
            else:
                result = error_message
            if result == 'exit':
                action = False
            else:
                print(result)


if __name__ == '__main__':
    main()
