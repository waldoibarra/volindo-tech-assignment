import sys

class CommandsOrquestator():
    valid_commands = ["part-1"]

    def __init__(self):
        self.validate_arguments(sys.argv)
        self.command = sys.argv[1]

    def run(self):
        match self.command:
            case "part-1":
                pass

    def validate_arguments(self, arguments):
        args_length = len(arguments)

        if args_length <= 1 or args_length > 2:
            self.exit("You misused the CLI, try using Makefile commands.")

        command = arguments[1]

        if command not in self.valid_commands:
            self.exit("{} is not a valid command.".format(command))

    def exit(self, message):
        print(message)
        sys.exit(1)
