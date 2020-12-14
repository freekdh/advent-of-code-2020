import re
from dataclasses import dataclass
from abc import abstractmethod
import math


def get_input_data(path_to_input_data):
    with open(path_to_input_data) as input_file:
        input_data = input_file.read().splitlines()
        return (
            int(input_data[0]),
            [int(bus_id) for bus_id in input_data[1].split(sep=",") if bus_id != "x"],
        )


def main():
    earliest_time_to_depart_on_bus, bus_ids = get_input_data(
        "advent_of_code_2020/day13/input.txt"
    )

    # Part 1:
    earliest_bus_id, departs_in_minutes = min(
        (
            (bus_id, bus_id - earliest_time_to_depart_on_bus % bus_id)
            for bus_id in bus_ids
        ),
        key=lambda x: x[1],
    )

    result1 = earliest_bus_id * departs_in_minutes
    print(f"Part1: result = {result1}")

    # Part 2:


if __name__ == "__main__":
    main()