from abc import ABC, abstractmethod
from classes import ValidationException
import argparse


class Command(ABC):
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.prepare_parser(self.parser)

    def validate_args(self, args):
        return None

    def get_args(self):
        return [a.option_strings for a in self.parser._actions]

    def executor(self, address_book, note_book, args):
        try:
            parsed = self.parser.parse_args(args)
            error = self.validate_args(parsed)
            if error is not None:
                return f"Error: {error}"

            return self.execute(address_book, note_book, parsed)

        except ValidationException as e:
            return f"Validation: {e.message}"

        except SystemExit:
            return None

    def prepare_parser(self, parser):
        pass

    def execute(self, address_book, note_book, args):
        pass
