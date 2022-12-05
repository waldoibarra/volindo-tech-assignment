import os

from interfaces.cli import CommandsOrquestator


class Main():
    def start(self):
        self.show_welcome_message()

        a = CommandsOrquestator()
        a.run()

    def show_welcome_message(self):
        self.clear()
        print("Welcome to my solution!")

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')


Main().start()
