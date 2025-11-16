from argparse import _SubParsersAction, ArgumentParser, Namespace
from commands.command import Command
from database import EmbeddingDatabase


class RenameCommand(Command):
    def __init__(self):
        super().__init__("rename")
    
    def setup_parser(self, sub_parser: _SubParsersAction[ArgumentParser]):
        rename_parser = sub_parser.add_parser(self.get_name(),
            description="Changes the name of a class."
        )
        rename_parser.add_argument("old_name",
            help="the name of the current class to change"                           
        )
        rename_parser.add_argument("new_name",
            help="the new name to change to"
        )

    def execute(self, args: Namespace):
        old_name, new_name = (args.old_name, args.new_name)

        print("Renaming class...")
        with EmbeddingDatabase() as database:
            update_count = database.rename_class(old_name, new_name)

        print(f"{update_count} documents updated. Done!")       