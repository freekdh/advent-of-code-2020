import re


def get_raw_input_data(path_to_input_data):
    with open(path_to_input_data) as input_file:
        return input_file.read().splitlines()


def get_row_number(raw_row_pattern):
    return int(
        (raw_row_pattern.replace("F", "0").replace("B", "1")),
        2,
    )


def get_column_number(raw_column_pattern):
    return int(
        (raw_column_pattern.replace("R", "1").replace("L", "0")),
        2,
    )


def get_seat_id(row, column):
    return row * 8 + column


class NoPassportFound(Exception):
    pass


def get_boarding_pass(row, column, boarding_passes):
    try:
        return next(
            boarding_pass
            for boarding_pass in boarding_passes
            if boarding_pass["row"] == row and boarding_pass["column"] == column
        )
    except StopIteration:
        raise NoPassportFound


def main():
    input_data = get_raw_input_data("advent_of_code_2020/day5/input.txt")

    # part 1
    boarding_passes = []
    for data in input_data:
        pattern = re.compile(pattern="([B|F]{7})([R|L]{3})")
        raw_row, raw_column = re.match(pattern=pattern, string=data).groups()

        row = get_row_number(raw_row)
        column = get_column_number(raw_column)
        seat_id = get_seat_id(row, column)

        boarding_passes.append({"row": row, "column": column, "seat_id": seat_id})

    highest_seat_id = max(boarding_pass["seat_id"] for boarding_pass in boarding_passes)

    print(f"Part1: highest seat ID on a boarding pass is: {highest_seat_id}")

    # part 2

    missing_boarding_passes = []
    for row in range(1, 126):
        for column in range(8):
            try:
                get_boarding_pass(row, column, boarding_passes)
            except NoPassportFound:
                seat_id = get_seat_id(row, column)
                missing_boarding_passes.append(
                    {"row": row, "column": column, "seat_id": seat_id}
                )

    missing_boarding_pass = [
        boarding_pass2
        for boarding_pass1, boarding_pass2, boarding_pass3 in zip(
            missing_boarding_passes,
            missing_boarding_passes[1:],
            missing_boarding_passes[2:],
        )
        if (
            boarding_pass1["seat_id"] + 1
            != boarding_pass2["seat_id"]
            != boarding_pass3["seat_id"] - 1
        )
    ]

    assert len(missing_boarding_pass) == 1

    missing_seat_id = missing_boarding_pass[0]["seat_id"]

    print(f"Part2: my missing seat ID is: {missing_seat_id}")


if __name__ == "__main__":
    main()