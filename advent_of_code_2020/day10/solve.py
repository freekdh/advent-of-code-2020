from collections import Counter
from networkx import nx


def get_input_data(path_to_input_data):
    with open(path_to_input_data) as input_file:
        return list(map(int, input_file.read().splitlines()))


def get_reachable_nodes(node, input_data):
    return [node + i for i in range(1, 4) if node + i in input_data]


def main():
    input_data = get_input_data("advent_of_code_2020/day10/input.txt")

    wall_jolt = 0
    device_jolt = max(input_data) + 3

    # Part 1
    input_data.append(wall_jolt)
    input_data.append(device_jolt)
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

    # Part 2
    n_paths_ending_in_last_node = {device_jolt: 1}
    for node in iter(reversed(input_data[:-1])):
        n_paths_ending_in_last_node[node] = sum(
            n_paths_ending_in_last_node[reachable_node]
            for reachable_node in get_reachable_nodes(node, input_data)
        )

    result_part2 = n_paths_ending_in_last_node[0]
    print(
        f"Part2: {result_part2} number of distinct ways you can arrange the adapters to connect the charging outlet to your device "
    )


if __name__ == "__main__":
    main()