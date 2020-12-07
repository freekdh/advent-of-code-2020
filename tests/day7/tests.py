from advent_of_code_2020.day7.solve import (
    get_raw_input_data,
    parse,
    get_directed_graph,
    get_n_bags_fit_in_bag,
)
from collections import ChainMap


def test_part2():
    raw_input_data = get_raw_input_data("tests/day7/test_data.txt")
    parsed_data = dict(ChainMap(*(parse(row) for row in raw_input_data)))
    graph = get_directed_graph(parsed_data)

    assert get_n_bags_fit_in_bag("shiny gold", graph) == 126