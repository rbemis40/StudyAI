from database import EmbeddingDatabase
from .command import Command

class RemoveCommand(Command):
    def __init__(self):
        super().__init__("remove", ["field", "value"])
    
    def execute(self, args: list[str]):
        field, value = args
        with EmbeddingDatabase() as database:
            database.remove_by_field(field, value)