from advent_of_code_2020.day14.solve import (
    parse,
    get_input_data,
    Computer,
    ComputerPart2,
)


def test():
    input_data = get_input_data("tests/day14/input.txt")
    commands = parse(input_data)

    computer = Computer(bitmask=commands[0].mask)
    assert 73 == computer._apply_bitmask(11)
    assert 101 == computer._apply_bitmask(101)
    assert 64 == computer._apply_bitmask(0)


def test_part2():
    input_data = get_input_data("tests/day14/input_part2.txt")
    commands = parse(input_data)
    computer = ComputerPart2()

    computer = ComputerPart2()
    for command in commands:
        computer.execute_command(command)

    assert 208 == sum(
        computer.get_value(memory_address)
        for memory_address in computer.get_written_memory_addresses()
    )
