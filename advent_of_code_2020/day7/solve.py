import re
from collections import ChainMap
import networkx as nx


def get_raw_input_data(path_to_input_data):
    with open(path_to_input_data) as input_file:
        return input_file.read().splitlines()


def parse(row):

    pattern = re.compile(pattern="(.+) bags contain (.+).")
    bag, contents = re.match(pattern=pattern, string=row).groups()
    contents = contents.split(",")

    result = {bag: set()}

    pattern = re.compile(pattern=".*(\d+) (.+) bags?")
    for content in contents:
        match = re.match(pattern=pattern, string=content)
        if match:
            n_items, bag_type = match.groups()
            result[bag].add((int(n_items), bag_type))
        else:
            assert content == "no other bags"

    return result


def get_directed_graph(parsed_data):
    graph = nx.DiGraph()
    for bag, content in parsed_data.items():
        for content_quantity, content_bag in content:
            graph.add_edge(bag, content_bag, content_quantity=content_quantity)
    return graph


def get_n_bags_fit_in_bag(bag, graph):
    return sum(
        graph[bag][bag_]["content_quantity"]
        + graph[bag][bag_]["content_quantity"] * get_n_bags_fit_in_bag(bag_, graph)
        for bag_ in graph[bag]
    )


def main():
    raw_input_data = get_raw_input_data(
        path_to_input_data="advent_of_code_2020/day7/input.txt"
    )

    parsed_data = dict(ChainMap(*(parse(row) for row in raw_input_data)))

    # Part1
    graph = get_directed_graph(parsed_data)
    reversed_graph = graph.reverse()
    successor_nodes = nx.nodes(nx.bfs_tree(reversed_graph, "shiny gold"))

    print(
        f"{len(successor_nodes)-1} bag colors can eventually contain at least one shiny gold bag "
    )

    # Part2
    n_bags_fig_in_shiny_gold = get_n_bags_fit_in_bag("shiny gold", graph)

    print(
        f"{n_bags_fig_in_shiny_gold} individual bags are required inside my single shiny gold bag "
    )


if __name__ == "__main__":
    main()
