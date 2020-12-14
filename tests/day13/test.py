from advent_of_code_2020.day13.solve import get_input_data


def test():
    earliest_time_to_depart_on_bus, bus_ids = get_input_data("tests/day13/input.txt")

    earliest_bus_id, departs_in_minutes = min(
        (
            (bus_id, bus_id - earliest_time_to_depart_on_bus % bus_id)
            for bus_id in bus_ids
        ),
        key=lambda x: x[1],
    )

    assert earliest_bus_id == 59
    assert departs_in_minutes == 5

    result1 = earliest_bus_id * departs_in_minutes
    assert result1 == 295