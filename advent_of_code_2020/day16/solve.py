from dataclasses import dataclass
import re


def get_input_data(path_to_input_data):
    with open(path_to_input_data) as input_file:
        input_file = input_file.read().split("\n\n")
        return [input_block.splitlines() for input_block in input_file]


@dataclass
class RangeRule:
    low_value: int
    high_value: int


@dataclass
class Rule:
    name: str
    range_rules: list

    def is_valid(self, value):
        return any(
            range_rule.low_value <= value <= range_rule.high_value
            for range_rule in self.range_rules
        )


@dataclass
class Ticket:
    values: list


def parse_rules(input_data):
    rules = []
    for row in input_data:
        pattern = re.compile(pattern="(.+): (\d+)-(\d+) or (\d+)-(\d+)")
        match = re.match(pattern=pattern, string=row)
        name, low_value_1, high_value_1, low_value_2, high_value_2 = match.groups()
        rules.append(
            Rule(
                name=name,
                range_rules=[
                    RangeRule(low_value=int(low_value_1), high_value=int(high_value_1)),
                    RangeRule(low_value=int(low_value_2), high_value=int(high_value_2)),
                ],
            )
        )
    return rules


def parse_my_ticket(input_data):
    return Ticket(values=list(map(int, input_data[1].split(sep=","))))


def parse_nearby_tickets(input_data):
    return [Ticket(values=list(map(int, row.split(sep=",")))) for row in input_data[1:]]


class TicketScanner:
    def __init__(self, rules):
        self.rules = rules

        self._scan_error_rate = 0

    @property
    def scan_error_rate(self):
        return self._scan_error_rate

    def scan(self, ticket):
        for value in ticket.values:
            if not self._valid_value(value):
                self._scan_error_rate += value

    def _valid_value(self, value):
        return any(rule.is_valid(value) for rule in self.rules)


def main():
    input_data = get_input_data("advent_of_code_2020/day16/input.txt")
    rules = parse_rules(input_data[0])
    my_ticket = parse_my_ticket(input_data[1])
    nearby_tickets = parse_nearby_tickets(input_data[2])

    ticket_scanner = TicketScanner(rules)
    for ticket in nearby_tickets:
        ticket_scanner.scan(ticket)

    print(f"Part1: the scan error is {ticket_scanner.scan_error_rate}")


if __name__ == "__main__":
    main()