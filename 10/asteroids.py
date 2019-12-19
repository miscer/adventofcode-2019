import collections
import itertools
import math
import sys
from typing import Tuple, TextIO, Set

Vector = Tuple[float, float]
Map = Tuple[Vector, Set[Vector]]


def parse_map(input: TextIO) -> Map:
    positions = set()
    width = 0
    height = 0

    for y, line in enumerate(input):
        points = list(line.strip())
        width = len(points)
        height += 1

        for x, point in enumerate(points):
            if point == '#':
                positions.add((x, y))

    return (width, height), positions


def vector_add(a: Vector, b: Vector) -> Vector:
    (x1, y1), (x2, y2) = a, b
    return x1 + x2, y1 + y2


def vector_subtract(a: Vector, b: Vector) -> Vector:
    (x1, y1), (x2, y2) = a, b
    return x1 - x2, y1 - y2


def vector_multiply(a: Vector, n: int) -> Vector:
    x, y = a
    return x * n, y * n


def vector_magnitude(vector: Vector) -> float:
    x, y = vector
    return math.sqrt(x ** 2 + y ** 2)


def vector_normalize(vector: Vector) -> Vector:
    x, y = vector
    m = vector_magnitude(vector)
    return x / m, y / m


def vector_round(vector: Vector, ndigits=None) -> Vector:
    x, y = vector
    return round(x, ndigits), round(y, ndigits)


def count_visible_asteroids(map: Map, position: Vector) -> int:
    size, positions = map
    groups = collections.defaultdict(list)

    for other in positions:
        if other != position:
            direction = vector_round(vector_normalize(vector_subtract(other, position)), 7)
            groups[direction].append(other)

    return len(groups.keys())


def print_visible(map: Map):
    (width, height), positions = map

    for y in range(height):
        for x in range(width):
            if (x, y) in positions:
                num_visible = count_visible_asteroids(map, (x, y))
                print(num_visible, end='')
            else:
                print('.', end='')

        print()


map = parse_map(sys.stdin)
size, positions = map

max_visible = max(count_visible_asteroids(map, p) for p in positions)
print(max_visible)
