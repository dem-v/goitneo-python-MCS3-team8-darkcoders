from .Command import Command


class HelloCommand(Command):
    def prepare_parser(self, parser):
        pass

    def execute(self, *_):
        return "Hello! How can I help you?"
