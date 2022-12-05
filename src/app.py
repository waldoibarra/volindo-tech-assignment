from src.interfaces.cli import CommandsOrquestator


class App():
    def execute(self):
        orquestator = CommandsOrquestator()
        orquestator.execute()
