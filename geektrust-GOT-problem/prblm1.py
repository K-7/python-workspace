import models


class Processor(models.BaseProcessor):

    def __process_message(self, sender, receiver, message_obj):
        if message_obj.did_message_map_emblem():
            self.allies.append(receiver)
            if len(self.allies) > 2:
                self.ruler = sender

    def process_input(self, input):
        if input == 'Who is the ruler of Southeros?':
            return self.ruler
        elif input == 'Allies of Ruler?':
            return self.allies or None
        else:
            name, message_txt = input.split(', ')
            kingdom = self.get_kingdom(name)
            ruler_kingdom = self.get_kingdom('space')
            message_txt = message_txt.replace('"', '')
            message_obj = self.get_message_obj(ruler_kingdom, kingdom, message_txt)
            self.__process_message(ruler_kingdom, kingdom, message_obj)
            return -1

    def print_output(self, output):
        if output != -1:
            if type(output) == models.Kingdom and output.name == 'space':
                print('Output: King Shan')
            elif type(output) == list:
                output_allies = [out.display_name for out in output]
                print('Output: {0}'.format(', '.join(output_allies)))
            else:
                print('Output: {0}'.format(output))


def main():
    output = None
    processor = Processor()
    while True:
        user_input = input('Input: ')
        if user_input:
            output = processor.process_input(user_input)
            processor.print_output(output)


if __name__ == '__main__':
    main()
