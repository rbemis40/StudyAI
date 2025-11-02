import sys
from dotenv import load_dotenv
from commands import *
    

def print_usage(prog_name: str, commands: list[Command]):
    for command in commands:
        print(command.get_usage(prog_name))

if __name__ == "__main__":
    commands = [
        ProcessCommand(),
        SearchCommand(),
        RemoveCommand(),
        ListByClassCommand(),
		ListClassesCommand(),
        RenameCommand()
    ]

    if len(sys.argv) < 2:
        print_usage(sys.argv[0], commands)
        sys.exit(-1)
    
    load_dotenv()

    given_command = sys.argv[1]   
    for command in commands:
        if command.is_valid(given_command, len(sys.argv) - 2):
            command.execute(sys.argv[2:])
            break
    else:
        print_usage(sys.argv[0], commands)
        sys.exit(-1)
