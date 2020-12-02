import re


def get_input_data():
    with open("02-12-2020/input.txt") as input_file:
        return input_file.read().splitlines()


def main():
    input_data = get_input_data()

    # part 1
    valid_passwords = 0
    for database_line in input_data:
        low_count, high_count, letter, password = re.match(
            pattern="(\d+)-(\d+)\s(.):\s(.*)", string=database_line
        ).groups()

        low_count, high_count = int(low_count), int(high_count)

        if low_count <= password.count(letter) <= high_count:
            valid_passwords += 1

    print(
        f"part1: {valid_passwords} valid passwords out of {len(input_data)} passwords"
    )

    # part 2

    valid_passwords = 0
    for database_line in input_data:
        first_digit, second_digit, letter, password = re.match(
            pattern="(\d+)-(\d+)\s(.):\s(.*)", string=database_line
        ).groups()

        first_digit, second_digit = int(first_digit), int(second_digit)

        if (password[first_digit - 1] == letter) != (
            password[second_digit - 1] == letter
        ):
            valid_passwords += 1

    print(
        f"part2: {valid_passwords} valid passwords out of {len(input_data)} passwords"
    )


if __name__ == "__main__":
    main()