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
    def __init__(self, bits=32, bitmask=None, memory={}):
        self._bits = bits
        self._bitmask = bitmask
        self._memory = memory

    def execute_command(self, command):
        self._update_bitmask(command)
        self._assign_value(command)

    def get_value(self, memory_address):
        return self._memory[memory_address]

    def get_written_memory_addresses(self):
        return (key for key, value in self._memory.items() if value)

    def _update_bitmask(self, command):
        if command.update_bit_mask():
            self._bitmask = command.mask
        else:
            pass

    def _assign_value(self, command):
        if command.assign_value():
            self._memory[command.memory_address] = self._apply_bitmask(command.value)
        else:
            pass

    def _apply_bitmask(self, integer):
        the_one_ = int(self._bitmask.replace("X", "1"), 2)
        the_zero_ = int(self._bitmask.replace("X", "0"), 2)
        return (integer & the_one_) | the_zero_


class ComputerPart2(Computer):
    def _get_variants(self, addr_mask):
        if "X" in addr_mask:
            for r in ("0", "1"):
                yield from self._get_variants(addr_mask.replace("X", r, 1))
        else:
            yield addr_mask

    def _assign_value(self, command):
        if command.assign_value():

            transformed_memory_address = "{0:036b}".format(command.memory_address)
            transformed_memory_address_ = ""
            for index, letter in enumerate(self._bitmask):
                if letter == "1":
                    transformed_memory_address_ += "1"
                elif letter == "0":
                    transformed_memory_address_ += transformed_memory_address[index]
                else:
                    transformed_memory_address_ += "X"

            for memory_address in self._get_variants(transformed_memory_address_):
                self._memory[int(memory_address, 2)] = command.value
        else:
            pass


def main():
    input_data = get_input_data("advent_of_code_2020/day14/input.txt")
    commands = parse(input_data)

    computer = Computer()
    for command in commands:
        computer.execute_command(command)

    result_part1 = sum(
        computer.get_value(memory_address)
        for memory_address in computer.get_written_memory_addresses()
    )

    print(
        f"Part1, {result_part1} is the sum of all values left in memory after it completes"
    )

    computer2 = ComputerPart2(memory={})
    for command in commands:
        computer2.execute_command(command)

    result_part2 = sum(
        computer2.get_value(memory_address)
        for memory_address in computer2.get_written_memory_addresses()
    )

    print(
        f"Part2, {result_part2} is the sum of all values left in memory after it completes"
    )


if __name__ == "__main__":
    main()