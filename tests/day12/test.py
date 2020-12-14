from advent_of_code_2020.day12.solve_part2 import *


def test():
    environment = Environment()
    environment.apply_action(F(10))
    assert environment.current_location == Location(100, 10)

    environment.apply_action(N(3))
    assert environment._relative_current_location_waypoint == Location(10, 4)
    assert environment.current_location == Location(100, 10)

    environment.apply_action(R(90))
    assert environment._relative_current_location_waypoint == Location(4, -10)
