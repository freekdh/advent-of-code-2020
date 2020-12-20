import re
from dataclasses import dataclass
import math
from itertools import chain, combinations
from copy import copy


def get_input_data(path_to_input_data):
    with open(path_to_input_data) as input_file:
        return input_file.read().splitlines()


def parse(input_data):
    commands = []
    for command in input_data:
        if "mask" in command:
            commands.append(Mask(mask=command[7:]))
        else:
            pattern = re.compile(pattern="mem.(\d+). = (\d+)")
            match = re.match(pattern=pattern, string=command)
            memory_address, value = match.groups()
            commands.append(
                AssignmentOperation(
                    memory_address=int(memory_address), value=int(value)
                )
            )
    return commands


@dataclass(frozen=True)
class Mask:
    mask: str

    def update_bit_mask(self):
        return True

    def assign_value(self):
        return False


@dataclass(frozen=True)
class AssignmentOperation:
    memory_address: int
    value: int

    def update_bit_mask(self):
        return False

    def assign_value(self):
        return True


class Computer:
    def __init__(self, foo=dict()):
        self._foo = foo

    def execute_command(self, mem, val):
        self._foo[mem] = val


class ComputerPart2(Computer):
    pass


def main():
    computer = Computer()
    computer.execute_command(10, 50)

    computer2 = ComputerPart2()
    print(computer2._foo)


if __name__ == "__main__":
    main()