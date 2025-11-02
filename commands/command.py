class Command:
    def __init__(self, name: str, arg_names: list[str]):
        self.name = name
        self.arg_names = arg_names

    def get_usage(self, prog_name: str) -> str:
        arg_str = []
        for arg in self.arg_names:
            arg_str.append(f"[{arg}]")

        return f"Usage: python {prog_name} {self.name} {' '.join(arg_str)}"

    def is_valid(self, given_name: str, num_args: int) -> bool:
        return given_name == self.name and num_args == len(self.arg_names) 

    def execute(args: list[str]):
        raise NotImplementedError('Command.execute must be implemented by child class')