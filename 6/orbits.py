import sys
from collections import defaultdict


def parse_input(input):
    for line in input:
        a, b = line.strip().split(')')
        yield a, b


def create_graph(orbits):
    graph = defaultdict(lambda: [])

    for a, b in orbits:
        graph[a].append(b)

    return graph


def find_path(graph, start_key, target_key):
    if start_key == target_key:
        return [start_key]

    for child_key in graph[start_key]:
        path = find_path(graph, child_key, target_key)

        if path is not None:
            return [start_key] + path

    return None


def count_transfers(path_a, path_b):
    for i in range(min(len(path_a), len(path_b))):
        if path_a[i] != path_b[i]:
            return len(path_a) + len(path_b) - 2 * (i + 1)


orbits = parse_input(sys.stdin)
graph = create_graph(orbits)

path_a = find_path(graph, 'COM', 'YOU')
path_b = find_path(graph, 'COM', 'SAN')

print(count_transfers(path_a, path_b))
