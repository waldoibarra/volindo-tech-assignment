import os
import sys

from ...application import Part1Action
from ...infrastructure.adult_50k_dataset import Adult50kDataset


class CommandsOrquestator():
    valid_commands = ["part-1"]

    def __init__(self):
        self.clear()
        self.validate_arguments(sys.argv)
        self.command = sys.argv[1]
        self.show_welcome_message()

    def execute(self):
        adult_50k_dataset = Adult50kDataset()

        match self.command:
            case "part-1":
                action = Part1Action(adult_50k_dataset)

        action.execute()

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def validate_arguments(self, arguments):
        args_length = len(arguments)

        if args_length <= 1 or args_length > 2:
            self.exit("You misused the CLI, try using Makefile commands.")

        command = arguments[1]

        if command not in self.valid_commands:
            self.exit("{} is not a valid command.".format(command))

    def show_welcome_message(self):
        self.clear()
        print("Welcome to my solution!")

    def exit(self, message):
        print(message)
        sys.exit(1)
