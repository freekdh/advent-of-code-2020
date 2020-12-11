from advent_of_code_2020.day11.solve import (
    get_input_data,
    Grid,
    Location,
    get_rule1_locations,
    get_rule2_locations,
    update_grid,
)


def test_location():
    input_data = get_input_data("tests/day11/test_input_data.txt")
    input_grid = Grid(input_data)

    assert len(list(input_grid.get_neighbours(Location(0, 0)))) == 3


def test_integration():
    input_data = get_input_data("tests/day11/test_input_data.txt")
    output_data = get_input_data("tests/day11/test_results_data.txt")

    input_grid = Grid(input_data)
    output_grid = Grid(output_data)

    current_grid = input_grid
    while True:
        new_grid = update_grid(current_grid)

        if current_grid == new_grid:
            break
        else:
            current_grid = new_grid

    assert new_grid == output_grid
