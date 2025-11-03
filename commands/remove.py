from argparse import _SubParsersAction, ArgumentParser, Namespace
from database import EmbeddingDatabase
from .command import Command

class RemoveCommand(Command):
    def __init__(self):
        super().__init__("remove")

    def setup_parser(self, sub_parser: _SubParsersAction[ArgumentParser]):
        remove_parser = sub_parser.add_parser(self.get_name(),
            description="Deletes a stored object based on one of it's fields."    
        )
        remove_parser.add_argument("field",
            help="the name of the field to check for the value"
        )
        remove_parser.add_argument("value",
            help="the value that deletes the object upon a match"
        )

    def execute(self, args: Namespace):
        field, value = (args.field, args.value)
        with EmbeddingDatabase() as database:
            database.remove_by_field(field, value)