from database import EmbeddingDatabase
from .command import Command

class ListCommand(Command):
    def __init__(self):
        super().__init__('list', ['class name'])
    
    def execute(self, args: list[str]):
        class_name, = args

        print("Getting unique titles...")
        with EmbeddingDatabase() as database:
            titles = database.get_doc_titles_for_class(class_name)

        print("\n")
        for title in titles:
            print(title)

        print("\nDone!")