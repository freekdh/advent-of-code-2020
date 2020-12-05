from advent_of_code_2020.day5.solve import (
    get_row_number,
    get_column_number,
    get_seat_id,
)


def test_get_row_number():
    assert get_row_number("BFFFBBF") == 70
    assert get_row_number("FFFBBBF") == 14
    assert get_row_number("BBFFBBF") == 102


def test_get_column_number():
    assert get_column_number("RRR") == 7
    assert get_column_number("RLL") == 4


def test_get_seat_id():
    assert get_seat_id(70, 7) == 567
    assert get_seat_id(14, 7) == 119
    assert get_seat_id(102, 4) == 820