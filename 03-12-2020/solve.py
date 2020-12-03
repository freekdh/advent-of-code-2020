import numpy as np


def get_raw_input_data():
    with open("03-12-2020/input.txt") as input_file:
        return input_file.read().splitlines()


def get_matrix(raw_input_data):
    return np.array(list(map(list, raw_input_data)), dtype=str).T


class InvalidPositionException(Exception):
    pass


class Environment:
    def __init__(self, matrix):
        self.matrix = matrix

        self._shape = matrix.shape

        self._x_boundary = None
        self._y_boundary = self._shape[1]

    def get_path(self, start_position, angle):
        """
        Get path through environment
        """
        position_path = self._get_position_path(start_position, angle)
        return (self._get_value_at_position(position) for position in position_path)

    def _get_position_path(self, start_position, angle):
        assert self._is_valid_position(start_position)

        position_path = [start_position]

        current_position = start_position
        while True:
            try:
                current_position = self._get_next_position(current_position, angle)
                position_path.append(current_position)
            except InvalidPositionException:
                return position_path

    def _get_value_at_position(self, position):
        """
        Environment stretches out indefinately to the right
        """
        return self.matrix[(position[0] % self._shape[0], position[1])]

    def _get_next_position(self, current_position, angle):
        next_position = tuple(map(sum, zip(current_position, angle)))
        if self._is_valid_position(next_position):
            return next_position
        else:
            raise InvalidPositionException()

    def _is_valid_position(self, position):
        valid_x = position[0] < self._x_boundary if self._x_boundary else True
        valid_y = position[1] < self._y_boundary if self._y_boundary else True

        return valid_x and valid_y


def main():
    raw_input_data = get_raw_input_data()
    matrix = get_matrix(raw_input_data)

    angle = (3, 1)
    start_position = (0, 0)

    environment = Environment(matrix)
    path = environment.get_path(start_position=start_position, angle=angle)

    enountered_trees_on_path = sum(place == "#" for place in path)

    print(f"We encountered {enountered_trees_on_path} trees")


if __name__ == "__main__":
    main()