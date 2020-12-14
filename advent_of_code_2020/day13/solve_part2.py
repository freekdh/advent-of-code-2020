from itertools import count


def get_input_data(path_to_input_data):
    with open(path_to_input_data) as input_file:
        input_data = input_file.read().splitlines()
        return (
            int(input_data[0]),
            [bus_id for bus_id in input_data[1].split(sep=",")],
        )


def main():
    earliest_time_to_depart_on_bus, bus_ids = get_input_data(
        "advent_of_code_2020/day13/input.txt"
    )

    data = (
        (index, int(bus_id)) for index, bus_id in enumerate(bus_ids) if bus_id.isdigit()
    )

    pattern_repeat_itself_n_steps = 1
    start_time = 0
    for index, bus_id in data:
        start_time = next(
            t
            for t in count(start_time, pattern_repeat_itself_n_steps)
            if (t + index) % bus_id == 0
        )
        pattern_repeat_itself_n_steps *= bus_id

    print(f"Part2: {start_time}")


if __name__ == "__main__":
    main()