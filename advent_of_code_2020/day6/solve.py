import re


def get_raw_input_data(path_to_input_data):
    with open(path_to_input_data) as input_file:
        return list(
            map(lambda s: s.split(sep="\n"), input_file.read().split(sep="\n\n"))
        )


def main():
    raw_input_data = get_raw_input_data(
        path_to_input_data="advent_of_code_2020/day6/input.txt"
    )

    # part 1
    result_part_1 = sum(
        len(list(set.union(*(set(list(member)) for member in group))))
        for group in raw_input_data
    )

    print(
        f"Part1: sum of counts for groups answered yes to any questions: {result_part_1}"
    )

    # part 1
    result_part_2 = sum(
        len(list(set.intersection(*(set(list(member)) for member in group))))
        for group in raw_input_data
    )

    print(
        f"Part2: sum of counts for groups answered yes to every questions: {result_part_2}"
    )


if __name__ == "__main__":
    main()
