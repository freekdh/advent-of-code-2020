from advent_of_code_2020.day11.solve import get_input_data, Grid as G, Location
from copy import deepcopy
from itertools import product


class NoSeat(Exception):
    pass


class Grid(G):
    def get_first_seat_in_direction(self, location, dx, dy):
        current_location = location
        while True:
            current_location = Location(
                current_location.x + dx, current_location.y + dy
            )
            if self.valid_location(current_location):
                if not self.is_floor(current_location):
                    return current_location
                else:
                    continue
            else:
                raise NoSeat()

    def get_see_seats(self, location):
        for dx, dy in product(range(-1, 2), range(-1, 2)):
            if dx != 0 or dy != 0:
                try:
                    yield self.get_first_seat_in_direction(location, dx, dy)
                except NoSeat:
                    pass


def get_rule1_locations(grid):
    """
    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    """
    for location in grid.get_locations():
        if grid.is_empty(location) and all(
            not grid.is_occupied(neighbour)
            for neighbour in grid.get_see_seats(location)
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
                for neighbour in grid.get_see_seats(location)
            )
            >= 5
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

    # Part 2
    current_grid = grid
    while True:
        new_grid = update_grid(current_grid)
        if current_grid == new_grid:
            break
        else:
            current_grid = new_grid

    result_part2 = sum(
        current_grid.is_occupied(location) for location in current_grid.get_locations()
    )

    print(f"{result_part2} seats are occupied seats")


if __name__ == "__main__":
    main()
