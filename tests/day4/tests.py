from advent_of_code_2020.day4.solve import get_input_data, get_passports


def test_valid_passports():
    input_data = get_input_data("tests/day4/test_valid_passports.txt")

    passports = get_passports(input_data)

    n_valid_passports = sum(
        (
            passport.required_fields_are_present()
            and passport.required_fields_are_valid()
        )
        for passport in passports
    )

    assert n_valid_passports == len(passports)


def test_invalid_passports():
    input_data = get_input_data("tests/day4/test_invalid_passports.txt")

    passports = get_passports(input_data)

    n_valid_passports = sum(
        (
            passport.required_fields_are_present()
            and passport.required_fields_are_valid()
        )
        for passport in passports
    )

    assert n_valid_passports == 0