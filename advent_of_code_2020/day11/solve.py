from itertools import product
from dataclasses import dataclass
from copy import deepcopy


def get_input_data(path_to_input_data):
    with open(path_to_input_data) as input_file:
        return list(map(list, input_file.read().splitlines()))


@dataclass(frozen=True, eq=True)
class Location:
    x: int
    y: int


class Grid:
    EMPTY = "L"
    OCCUPIED = "#"
    FLOOR = "."

    def __init__(self, input_data):
        self.input_data = input_data
        self.n_x = len(self.input_data[0])
        self.n_y = len(self.input_data)

    def __eq__(self, other):
        return self.input_data == other.input_data

    def empty_seat(self, location):
        self.input_data[location.y][location.x] = Grid.EMPTY

    def occupy_seat(self, location):
        self.input_data[location.y][location.x] = Grid.OCCUPIED

    def is_occupied(self, location):
        return True if self.input_data[location.y][location.x] == "#" else False

    def is_empty(self, location):
        return True if self.input_data[location.y][location.x] == "L" else False

    def is_floor(self, location):
        return True if self.input_data[location.y][location.x] == "." else False

    def get_locations(self):
        return (
            Location(x=x, y=y) for x, y in product(range(self.n_x), range(self.n_y))
        )

    def valid_location(self, location):
        return 0 <= location.x < self.n_x and 0 <= location.y < self.n_y

    def get_neighbours(self, location):
        return (
            Location(x=location.x + dx, y=location.y + dy)
            for dx, dy in product(range(-1, 2), range(-1, 2))
            if (dx != 0 or dy != 0)
            and self.valid_location(Location(x=location.x + dx, y=location.y + dy))
        )


def get_rule1_locations(grid):
    """
    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    """
    for location in grid.get_locations():
        if grid.is_empty(location) and all(
            not grid.is_occupied(neighbour)
            for neighbour in grid.get_neighbours(location)
        ):
            yield location


def get_rule2_locations(grid):
    """
    If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty
    """
    for location in grid.get_locations():
        if (
            grid.is_occupied(location)
            and sum(
                grid.is_occupied(neighbour)
                for neighbour in grid.get_neighbours(location)
            )
            >= 4
        ):
            yield location


def update_grid(grid):
    new_grid = deepcopy(grid)
    rule1_locations = list(get_rule1_locations(new_grid))
    rule2_locations = list(get_rule2_locations(new_grid))
    assert len(set(rule1_locations).intersection(set(rule2_locations))) == 0

    for location in rule1_locations:
        new_grid.occupy_seat(location)

    for location in rule2_locations:
        new_grid.empty_seat(location)

    return new_grid


def main():
    input_data = get_input_data("advent_of_code_2020/day11/input.txt")

    grid = Grid(input_data)

    # Part 1
    current_grid = grid
    while True:
        new_grid = update_grid(current_grid)

        if current_grid == new_grid:
            break
        else:
            current_grid = new_grid

    result_part1 = sum(
        current_grid.is_occupied(location) for location in current_grid.get_locations()
    )

    print(f"{result_part1} seats are occupied seats")

    # Part2


if __name__ == "__main__":
    main()
