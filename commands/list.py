from argparse import _SubParsersAction, ArgumentParser, Namespace
from database import EmbeddingDatabase
from .command import Command

class ListCommand(Command):
    def __init__(self):
        super().__init__("list")

    def setup_parser(self, sub_parser: _SubParsersAction[ArgumentParser]):
        list_parser = sub_parser.add_parser(self.get_name(),
            description="Lists previously created classes or documents."
        )
        list_parser.add_argument("--classname",
            help="show a list of document titles for the class"                         
        )
    
    def execute(self, args: Namespace):
        if (name := args.classname) is None:
            self._list_classes()
        else:
            self._list_by_class(name)

    def _list_classes(self):
        print("Getting unique class names...")
        with EmbeddingDatabase() as database:
            classes = database.get_class_names()

        print("")
        for class_name in classes:
            print(class_name)

        print("\nDone!")

    def _list_by_class(self, class_name: str):
        print("Getting unique titles...")
        with EmbeddingDatabase() as database:
            titles = database.get_doc_titles_for_class(class_name)

        print("")
        for title in titles:
            print(title)

        print("\nDone!")
