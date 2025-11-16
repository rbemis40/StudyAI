from argparse import _SubParsersAction, ArgumentParser, Namespace


class Command:
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

    def setup_parser(self, sub_parser: _SubParsersAction[ArgumentParser]):
        raise NotImplementedError("Command.setup_parser must be implemented by child class")

    def execute(self, args: Namespace):
        raise NotImplementedError("Command.execute must be implemented by child class")