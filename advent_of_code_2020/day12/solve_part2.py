from advent_of_code_2020.day12.solve import get_input_data
from dataclasses import dataclass
import math


@dataclass
class Action:
    value: int

    def get_rotate_waypoint_delta(self):
        return 0

    def get_northsourth_delta(self):
        return 0

    def get_eastwest_delta(self):
        return 0

    def get_move(self):
        return 0


@dataclass
class N(Action):
    def get_northsourth_delta(self):
        return self.value


@dataclass
class S(Action):
    def get_northsourth_delta(self):
        return -self.value


@dataclass
class E(Action):
    def get_eastwest_delta(self):
        return self.value


@dataclass
class W(Action):
    def get_eastwest_delta(self):
        return -self.value


@dataclass
class L(Action):
    def get_rotate_waypoint_delta(self):
        return self.value


@dataclass
class R(Action):
    def get_rotate_waypoint_delta(self):
        return -self.value


@dataclass
class F(Action):
    def get_move(self):
        return self.value


@dataclass
class Location:
    x: int
    y: int


class Environment:
    def __init__(
        self,
        start_location_ship=Location(0, 0),
        relative_start_location_waypoint=Location(10, 1),
    ):
        """
        Orientation 0 -> East
        """
        self._original_location_ship = start_location_ship
        self._current_location_ship = start_location_ship
        self._relative_current_location_waypoint = relative_start_location_waypoint

    @property
    def current_location(self):
        return self._current_location_ship

    def apply_action(self, action):
        self.update_relative_location_waypoint(action)
        self.update_relative_orientation_waypoint(action)
        self.update_location_ship(action)

    def update_location_ship(self, action):
        value = action.get_move()
        self._current_location_ship = Location(
            x=self._current_location_ship.x
            + self._relative_current_location_waypoint.x * value,
            y=self._current_location_ship.y
            + self._relative_current_location_waypoint.y * value,
        )

    def update_relative_orientation_waypoint(self, action):
        value = action.get_rotate_waypoint_delta()
        sin_theta = int(math.sin(math.radians(value)))
        cos_theta = int(math.cos(math.radians(value)))

        x = self._relative_current_location_waypoint.x
        y = self._relative_current_location_waypoint.y

        self._relative_current_location_waypoint = Location(
            x=x * cos_theta - y * sin_theta, y=x * sin_theta + y * cos_theta
        )

    def update_relative_location_waypoint(self, action):
        delta_northsouth = action.get_northsourth_delta()
        delta_eastwest = action.get_eastwest_delta()
        self._relative_current_location_waypoint = Location(
            x=self._relative_current_location_waypoint.x + delta_eastwest,
            y=self._relative_current_location_waypoint.y + delta_northsouth,
        )

    def get_manhatten_distance(self):
        return abs(
            self._original_location_ship.x - self._current_location_ship.x
        ) + abs(self._original_location_ship.y - self._current_location_ship.y)


def main():
    actions = get_input_data("advent_of_code_2020/day12/input.txt")
    actions = [eval(action[0])(action[1]) for action in actions]

    environment = Environment()

    for action in actions:
        environment.apply_action(action)

    print(f"Part2: The manhattan distance is {environment.get_manhatten_distance()}")


if __name__ == "__main__":
    main()