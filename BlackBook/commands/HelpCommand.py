from .Command import Command


class HelpCommand(Command):
    def prepare_parser(self, parser):
        pass

    def execute(self, *_):
        return "Here will be help"
