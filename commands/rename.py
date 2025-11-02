from commands.command import Command
from database import EmbeddingDatabase


class RenameCommand(Command):
    def __init__(self):
        super().__init__("rename", ["old class name", "new class name"])
    
    def execute(self, args: list[str]):
        old_name, new_name = args

        print("Renaming class...")
        with EmbeddingDatabase() as database:
            update_count = database.rename_class(old_name, new_name)

        print(f"{update_count} documents updated. Done!")       