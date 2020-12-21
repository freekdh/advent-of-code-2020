from itertools import product


def get_input_data(path_to_input_data):
    with open(path_to_input_data) as input_file:
        return input_file.read().splitlines()


class PocketDimension:
    def __init__(self, initial_state):
        self.lookup_table = dict()  # key: (x,y,z), value = 1

        initial_state_x_len, initial_state_y_len = self._get_dimensions_state(
            initial_state
        )

        for x, y in product(range(initial_state_x_len), range(initial_state_y_len)):
            if initial_state[y][x] == "#":
                self.lookup_table[(x, initial_state_y_len - 1 - y, 0)] = 1

    def get_active_cells(self):
        return list(self.lookup_table.keys())

    def run_cycle(self):
        inactive_locations_to_be_checked = self._get_inactive_locations_to_be_checked()
        active_locations_to_be_checked = self._get_active_locations_to_be_checked()
        swap_to_active, swap_to_inactive = [], []
        for active_location in active_locations_to_be_checked:
            active_neighbours = self._get_n_active_neighbours(active_location)
            if not (active_neighbours == 2 or active_neighbours == 3):
                swap_to_inactive.append(active_location)

        for inactive_location in inactive_locations_to_be_checked:
            if self._get_n_active_neighbours(inactive_location) == 3:
                swap_to_active.append(inactive_location)

        for location in swap_to_active:
            self.lookup_table[location] = 1

        for location in swap_to_inactive:
            del self.lookup_table[location]

    def get_z_slice(self, index, x_range, y_range):
        z_slice = ""
        for y in reversed(range(y_range[0], y_range[1] + 1)):
            for x in range(x_range[0], x_range[1] + 1):
                if (x, y, index) in self.lookup_table:
                    z_slice += "#"
                else:
                    z_slice += "."
            z_slice += "\n"
        return z_slice

    def _get_dimensions_state(self, state):
        return (len(state[0]), len(state))

    def _get_active_locations_to_be_checked(self):
        return set(self.lookup_table.keys())

    def _get_inactive_locations_to_be_checked(self):
        inactive_locations = set()
        for key in self.lookup_table:
            for x, y, z in product(range(-1, 2), range(-1, 2), range(-1, 2)):
                if (x, y, z) != (0, 0, 0):
                    inactive_locations.add((key[0] + x, key[1] + y, key[2] + z))
        return inactive_locations

    def _get_n_active_neighbours(self, location):
        return sum(
            (location[0] + x, location[1] + y, location[2] + z) in self.lookup_table
            for x, y, z in product(range(-1, 2), range(-1, 2), range(-1, 2))
            if (x, y, z) != (0, 0, 0)
        )


def main():
    input_data = get_input_data("advent_of_code_2020/day17/input.txt")
    pocket_dimension = PocketDimension(input_data)

    for cycle in range(6):
        pocket_dimension.run_cycle()

    n_active_cubes = len(pocket_dimension.get_active_cells())

    print(
        f"Part1: {n_active_cubes} cubes are left in the active state after the sixth cycle"
    )


if __name__ == "__main__":
    main()