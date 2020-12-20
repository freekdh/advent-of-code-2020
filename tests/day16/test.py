from advent_of_code_2020.day16.solve import (
    get_input_data,
    parse_my_ticket,
    parse_nearby_tickets,
    parse_rules,
    TicketScanner,
)


def test():
    input_data = get_input_data("tests/day16/input.txt")
    rules = parse_rules(input_data[0])
    my_ticket = parse_my_ticket(input_data[1])
    nearby_tickets = parse_nearby_tickets(input_data[2])

    ticket_scanner = TicketScanner(rules)
    for ticket in nearby_tickets:
        ticket_scanner.scan(ticket)

    assert ticket_scanner.scan_error_rate == 71