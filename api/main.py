import sys
from dotenv import load_dotenv
from commands import *
from commands.handler import CommandHandler
    

if __name__ == "__main__":
    load_dotenv()
    cmd_handler = CommandHandler("studyai", [
        ListCommand(),
        ProcessCommand(),
        RemoveCommand(),
        RenameCommand(),
        SearchCommand()
    ])

    cmd_handler.handle(sys.argv[1:])
