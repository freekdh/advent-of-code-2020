import requests
from itertools import combinations


def get_input_data():
    with open("01-12-2020/input.txt") as input_file:
        input_data = input_file.read().splitlines()
    return [int(value) for value in input_data]


def main():
    input_data = get_input_data()

    # part 1
    result_part1 = next(
        value1 * value2
        for value1, value2 in combinations(input_data, 2)
        if value1 + value2 == 2020
    )
    print(f"result part 1: {result_part1}")

    # part 2
    result_part2 = next(
        value1 * value2 * value3
        for value1, value2, value3 in combinations(input_data, 3)
        if value1 + value2 + value3 == 2020
    )
    print(f"result part 2: {result_part2}")


if __name__ == "__main__":
    main()