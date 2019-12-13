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


def count_orbits(graph, key, depth=0):
    return depth + sum(count_orbits(graph, child, depth + 1) for child in graph[key])


orbits = parse_input(sys.stdin)
graph = create_graph(orbits)

print(count_orbits(graph, 'COM'))
