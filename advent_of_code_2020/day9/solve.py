import re
from itertools import combinations


def get_input_data(path_to_input_data):
    with open(path_to_input_data) as input_file:
        return list(map(int, input_file.read().splitlines()))


def is_the_sum_of_two_of_the_n_numbers(focal_number, n_numbers):
    return any(
        number1 + number2 == focal_number
        for number1, number2 in combinations(n_numbers, 2)
    )


def get_window_iterator(list_of_data, window_size):
    return zip(*(list_of_data[n:] for n in range(window_size)))


def main():
    input_data = get_input_data("advent_of_code_2020/day9/input.txt")

    preamble = 25

    result_part1 = next(
        focal_numbers[-1]
        for focal_numbers in get_window_iterator(
            list_of_data=input_data, window_size=preamble + 1
        )
        if not is_the_sum_of_two_of_the_n_numbers(
            focal_number=focal_numbers[-1], n_numbers=focal_numbers[:-1]
        )
    )

    print(
        f"{result_part1} is the first number that is not the sum of two of the {preamble} preamble numbers before"
    )


if __name__ == "__main__":
    main()