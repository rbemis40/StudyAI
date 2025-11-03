from .command import Command
import argparse

class CommandHandler:
    def __init__(self, prog_name: str, commands: list[Command] = [], parser: argparse.ArgumentParser = None):
        if parser is None:
            self.parser = argparse.ArgumentParser(prog=prog_name)
        else:
            self.parser = parser

        self.sub_parser = self.parser.add_subparsers(dest="cmd", required=True)
        
        self.commands = {}
        for cmd in commands:
            self.add_command(cmd)

    def add_command(self, command: Command):
        if (name := command.get_name()) in self.commands:
            raise ValueError(f"Can not add command '{name}' to handler, command with same name already exists")
        
        command.setup_parser(self.sub_parser)
        self.commands[name] = command


    def handle(self, args: list[str]) -> bool:
        parse_results = self.parser.parse_args(args)
        if ("cmd" not in parse_results) or (parse_results.cmd not in self.commands):
            return False
        
        self.commands[parse_results.cmd].execute(parse_results)


