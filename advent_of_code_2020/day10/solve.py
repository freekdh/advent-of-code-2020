from collections import Counter


def get_input_data(path_to_input_data):
    with open(path_to_input_data) as input_file:
        return list(map(int, input_file.read().splitlines()))


def main():
    input_data = get_input_data("advent_of_code_2020/day10/input.txt")

    # Part 1
    input_data.append(0)
    input_data.append(max(input_data) + 3)
    input_data.sort()

    jumps = Counter(
        second_jolt - first_jolt
        for first_jolt, second_jolt in zip(input_data, input_data[1:])
    )

    assert jumps.keys() == set([1, 3])

    result_part1 = jumps[1] * jumps[3]

    print(
        f"Part1: {result_part1} 1-jolt differences multiplied by the number of 3-jolt differences"
    )


if __name__ == "__main__":
    main()