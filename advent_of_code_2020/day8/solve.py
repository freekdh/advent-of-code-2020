import re
from copy import copy


def get_input_data(path_to_input_data):
    with open(path_to_input_data) as input_file:
        raw_in = input_file.read().splitlines()

    pattern = re.compile(pattern="(.+) ([+-]{1})(\d+)")
    sequence_of_code = {}
    for index, line in enumerate(raw_in):
        groups = re.match(pattern, line).groups()
        sequence_of_code[index] = {
            "instruction": groups[0],
            "value": int(groups[2]) if groups[1] == "+" else (-1 * int(groups[2])),
        }

    return sequence_of_code


def get_covered_indices(from_index, input_data, accumulator=0):
    current_index = from_index
    accumulator = accumulator
    covered_indices = set()
    while True:
        if current_index in covered_indices:
            break
        else:
            try:
                current_instruction = input_data[current_index]
            except KeyError:
                break
            covered_indices.add(current_index)
            if current_instruction["instruction"] == "acc":
                accumulator += current_instruction["value"]
                current_index += 1
            elif current_instruction["instruction"] == "jmp":
                current_index += current_instruction["value"]
            elif current_instruction["instruction"] == "nop":
                current_index += 1
            else:
                raise Exception(f"don't recognize instruction {current_instruction}")

    return covered_indices, accumulator


def main():
    input_data = get_input_data("advent_of_code_2020/day8/input.txt")

    # Part 1
    covered_indices_part1, accumulator_part1 = get_covered_indices(
        from_index=0, accumulator=0, input_data=input_data
    )

    print(f"Part 1: the value of the accumulator is {accumulator_part1}")

    # Part 2
    for index in covered_indices_part1:
        if input_data[index]["instruction"] == "jmp":
            covered_indices_part2, _ = get_covered_indices(index + 1, input_data)
        elif input_data[index]["instruction"] == "nop":
            covered_indices_part2, _ = get_covered_indices(
                index + input_data[index]["value"], input_data
            )
        else:
            continue
        if len(input_data) - 1 in covered_indices_part2:
            break

    part2_input_data = copy(input_data)
    part2_input_data[index]["instruction"] = "nop"

    covered_indices_part2, accumulator_part2 = get_covered_indices(
        from_index=0, accumulator=0, input_data=part2_input_data
    )

    assert len(input_data) - 1 in covered_indices_part2

    print(f"Part 2: the value of the accumulator is {accumulator_part2}")


if __name__ == "__main__":
    main()