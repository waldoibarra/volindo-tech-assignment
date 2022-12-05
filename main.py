from src.interfaces.cli import CommandsOrquestator


class Main():
    def execute(self):
        orquestator = CommandsOrquestator()
        orquestator.execute()


Main().execute()
