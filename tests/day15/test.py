from advent_of_code_2020.day15.solve import Game


def test_integration():
    starting_numbers = [0, 3, 6]

    game = Game(starting_numbers)
    number_spoken = game.get_number_spoken(turn=2020)

    assert number_spoken == 436