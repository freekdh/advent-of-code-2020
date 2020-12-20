from dataclasses import dataclass
import re
import numpy as np


def get_input_data(path_to_input_data):
    with open(path_to_input_data) as input_file:
        input_file = input_file.read().split("\n\n")
        return [input_block.splitlines() for input_block in input_file]


@dataclass
class RangeRule:
    low_value: int
    high_value: int


@dataclass(frozen=True)
class Rule:
    name: str
    range_rules: list

    def __repr__(self):
        return self.name

    def __hash__(self):
        return id(self)

    def is_valid(self, value):
        return any(
            range_rule.low_value <= value <= range_rule.high_value
            for range_rule in self.range_rules
        )

    def name_start_with(self, string_):
        return string_ in self.name


@dataclass(frozen=True, eq=False)
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
        self._valid_tickets = set()

    @property
    def scan_error_rate(self):
        return self._scan_error_rate

    @property
    def valid_tickets(self):
        return self._valid_tickets

    def scan(self, ticket):
        valid_ticket = True
        for value in ticket.values:
            if not self._valid_value(value):
                valid_ticket = False
                self._scan_error_rate += value

        if valid_ticket:
            self._valid_tickets.add(ticket)

    def _valid_value(self, value):
        return any(rule.is_valid(value) for rule in self.rules)


def get_index_to_valid_rules(rules, tickets):
    return {
        ticket_index: {
            rule
            for rule in rules
            if all(rule.is_valid(ticket.values[ticket_index]) for ticket in tickets)
        }
        for ticket_index in range(len(list(tickets)[0].values))
    }


def get_rule_to_index(index_to_valid_rules, tickets):
    rule_to_index = {}
    for _ in range(len(list(tickets)[0].values)):
        for index, valid_rules in index_to_valid_rules.items():
            if len(valid_rules) == 1:
                rule = valid_rules.pop()
                rule_to_index[rule] = index
                for valid_rules_ in index_to_valid_rules.values():
                    valid_rules_.discard(rule)
    return rule_to_index


def main():
    input_data = get_input_data("advent_of_code_2020/day16/input.txt")
    rules = parse_rules(input_data[0])
    my_ticket = parse_my_ticket(input_data[1])
    nearby_tickets = parse_nearby_tickets(input_data[2])

    ticket_scanner = TicketScanner(rules)
    for ticket in nearby_tickets:
        ticket_scanner.scan(ticket)

    print(f"Part1: the scan error is {ticket_scanner.scan_error_rate}")

    # part 2
    valid_tickets = ticket_scanner.valid_tickets

    index_to_valid_rules = get_index_to_valid_rules(rules, valid_tickets)
    rule_to_index = get_rule_to_index(index_to_valid_rules, valid_tickets)

    result_part2 = np.prod(
        [
            my_ticket.values[index]
            for index in [
                rule_to_index[rule]
                for rule in rules
                if rule.name_start_with("departure")
            ]
        ]
    )

    print(f"Part2: the result for part 2 {result_part2}")


if __name__ == "__main__":
    main()