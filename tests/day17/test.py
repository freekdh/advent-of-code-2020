from advent_of_code_2020.day17.solve import get_input_data, PocketDimension


def test_initial_state():
    input_data = get_input_data("advent_of_code_2020/day17/input.txt")
    pocket_dimension = PocketDimension(initial_state=input_data)
    assert pocket_dimension.lookup_table[(1, 0, 0)] == 1
    assert pocket_dimension.lookup_table[(2, 0, 0)] == 1
    assert pocket_dimension.lookup_table[(4, 1, 0)] == 1
    assert pocket_dimension.lookup_table[(5, 1, 0)] == 1


def test_active_neighbours():
    input_data = get_input_data("advent_of_code_2020/day17/input.txt")
    pocket_dimension = PocketDimension(initial_state=input_data)

    assert pocket_dimension._get_n_active_neighbours((4, 1, 0)) == 3


def test_run_cycle():
    input_data = get_input_data("tests/day17/test_input.txt")

    pocket_dimension = PocketDimension(initial_state=input_data)

    assert (
        pocket_dimension.get_slice(
            other_dimensions=(0,), x_range=[0, 2], y_range=[0, 2]
        )
        == ".#.\n..#\n###\n"
    )

    pocket_dimension.run_cycle()

    assert (
        pocket_dimension.get_slice(
            other_dimensions=(-1,), x_range=[0, 2], y_range=[-1, 1]
        )
        == "#..\n..#\n.#.\n"
    )

    assert (
        pocket_dimension.get_slice(
            other_dimensions=(0,), x_range=[0, 2], y_range=[-1, 1]
        )
        == "#.#\n.##\n.#.\n"
    )

    assert (
        pocket_dimension.get_slice(
            other_dimensions=(1,), x_range=[0, 2], y_range=[-1, 1]
        )
        == "#..\n..#\n.#.\n"
    )

    pocket_dimension.run_cycle()

    assert (
        pocket_dimension.get_slice(
            other_dimensions=(-2,), x_range=[-1, 3], y_range=[-2, 2]
        )
        == ".....\n.....\n..#..\n.....\n.....\n"
    )

    assert (
        pocket_dimension.get_slice(
            other_dimensions=(-1,), x_range=[-1, 3], y_range=[-2, 2]
        )
        == "..#..\n.#..#\n....#\n.#...\n.....\n"
    )


def test_active_cubes():
    input_data = get_input_data("tests/day17/test_input.txt")

    pocket_dimension = PocketDimension(initial_state=input_data)

    for cycle in range(6):
        pocket_dimension.run_cycle()

    assert len(pocket_dimension.get_active_cells()) == 112


def test_4d_cycles():
    input_data = get_input_data("tests/day17/test_input.txt")

    pocket_dimension = PocketDimension(initial_state=input_data, dimensionality=4)

    pocket_dimension.run_cycle()

    assert (
        pocket_dimension.get_slice(
            other_dimensions=(-1, -1), x_range=[0, 2], y_range=[-1, 1]
        )
        == "#..\n..#\n.#.\n"
    )

    assert (
        pocket_dimension.get_slice(
            other_dimensions=(0, -1), x_range=[0, 2], y_range=[-1, 1]
        )
        == "#..\n..#\n.#.\n"
    )

    pocket_dimension.run_cycle()

    assert (
        pocket_dimension.get_slice(
            other_dimensions=(-2, -2), x_range=[-1, 3], y_range=[-2, 2]
        )
        == ".....\n.....\n..#..\n.....\n.....\n"
    )

    assert (
        pocket_dimension.get_slice(
            other_dimensions=(0, -2), x_range=[-1, 3], y_range=[-2, 2]
        )
        == "###..\n##.##\n#...#\n.#..#\n.###.\n"
    )

    assert (
        pocket_dimension.get_slice(
            other_dimensions=(-1, 0), x_range=[-1, 3], y_range=[-2, 2]
        )
        == ".....\n.....\n.....\n.....\n.....\n"
    )


def test_active_cubes_4d():
    input_data = get_input_data("tests/day17/test_input.txt")

    pocket_dimension = PocketDimension(initial_state=input_data, dimensionality=4)

    for cycle in range(6):
        pocket_dimension.run_cycle()

    assert len(pocket_dimension.get_active_cells()) == 848
