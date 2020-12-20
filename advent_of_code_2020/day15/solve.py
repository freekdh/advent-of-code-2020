from collections import defaultdict


class Game:
    def __init__(self, starting_numbers):
        assert len(starting_numbers) > 0
        self.starting_numbers = starting_numbers

        self._sequence = starting_numbers
        self._last_time_value_spoken = defaultdict(lambda: [])
        for index, start_number in enumerate(starting_numbers):
            self._last_time_value_spoken[start_number].append(index + 1)

    def get_number_spoken(self, turn):
        try:
            return self._sequence[turn - 1]
        except IndexError:
            self._play_until(turn)
            return self._sequence[turn - 1]

    def _get_last_turn(self):
        return len(self._sequence)

    def _play_until(self, until_turn):
        while self._get_last_turn() <= until_turn:
            if self._first_time_spoken(self._sequence[-1]):
                self._add_number(0)
            else:
                turns_apart = self._how_many_turns_ago(self._sequence[-1])
                self._add_number(turns_apart)

    def _how_many_turns_ago(self, value):
        return (
            self._last_time_value_spoken[value][-1]
            - self._last_time_value_spoken[value][-2]
        )

    def _first_time_spoken(self, value):
        return len(self._last_time_value_spoken[value]) == 1

    def _add_number(self, value):
        self._sequence.append(value)
        self._last_time_value_spoken[value].append(self._get_last_turn())

    def _get_last_number_spoken(self):
        pass


def main():
    puzzle_input = [17, 1, 3, 16, 19, 0]

    game = Game(puzzle_input)

    number_spoken_turn_2020 = game.get_number_spoken(turn=2020)

    print(f"Part1: {number_spoken_turn_2020} is the number spoken at turn 2020")


if __name__ == "__main__":
    main()