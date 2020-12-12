import re
from dataclasses import dataclass
from abc import abstractmethod
import math


def get_input_data(path_to_input_data):
    with open(path_to_input_data) as input_file:
        raw_data = input_file.read().splitlines()
        pattern = re.compile(pattern="([A-Z]{1})(\d+)")
        actions = [re.match(pattern, action).groups() for action in raw_data]
        return [(action[0], int(action[1])) for action in actions]


@dataclass
class Action:
    value: int

    def get_orientation_delta(self):
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
    def get_orientation_delta(self):
        return self.value


@dataclass
class R(Action):
    def get_orientation_delta(self):
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
    def __init__(self, start_position=Location(0, 0), start_orientation=0):
        """
        Orientation 0 -> East
        """
        self._original_location = start_position
        self._current_location = start_position
        self._current_orientation = start_orientation

    @property
    def current_location(self):
        return self._current_location

    def apply_action(self, action):
        self.update_current_location(action)
        self.update_current_orientation(action)
        self.update_move(action)

    def update_move(self, action):
        value = action.get_move()
        delta_northsouth = int(math.sin(math.radians(self._current_orientation)))
        delta_eastwest = int(math.cos(math.radians(self._current_orientation)))

        self._current_location = Location(
            x=self._current_location.x + delta_eastwest * value,
            y=self._current_location.y + delta_northsouth * value,
        )

    def update_current_orientation(self, action):
        delta = action.get_orientation_delta()
        self._current_orientation += delta

    def update_current_location(self, action):
        delta_northsouth = action.get_northsourth_delta()
        delta_eastwest = action.get_eastwest_delta()
        self._current_location = Location(
            x=self._current_location.x + delta_eastwest,
            y=self._current_location.y + delta_northsouth,
        )

    def get_manhatten_distance(self):
        return abs(self._original_location.x - self._current_location.x) + abs(
            self._original_location.y - self._current_location.y
        )


def main():
    actions = get_input_data("advent_of_code_2020/day12/input.txt")
    actions = [eval(action[0])(action[1]) for action in actions]

    environment = Environment()

    for action in actions:
        environment.apply_action(action)

    print(f"Part1: The manhattan distance is {environment.get_manhatten_distance()}")


if __name__ == "__main__":
    main()
