import sys
import argparse
from dotenv import load_dotenv
from commands import *
    

def print_usage(prog_name: str, commands: list[Command]):
    for command in commands:
        print(command.get_usage(prog_name))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="studyai")
    cmd_parser = parser.add_subparsers(dest="cmd", required=True)

    list_parser = cmd_parser.add_parser("list")
    list_parser.add_argument("--class", nargs=1)

    process_parser = cmd_parser.add_parser("process")
    process_parser.add_argument("pdf_path")
    process_parser.add_argument("class_name")
    process_parser.add_argument("doc_title")

    print(parser.parse_args(sys.argv[1:]))

    sys.exit(0)
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
