import itertools
import math
import sys
from typing import Tuple, TextIO, Set

Vector = Tuple[int, int]
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


def vector_shorten(a: Vector) -> Vector:
    x, y = a
    gcd = math.gcd(x, y)

    return math.floor(x / gcd), math.floor(y / gcd)


def within_bounds(vector: Vector, bounds: Vector) -> bool:
    x, y = vector
    max_x, max_y = bounds

    return 0 <= x < max_x and 0 <= y < max_y


def count_visible_asteroids(map: Map, position: Vector) -> int:
    size, positions = map
    others = {p for p in positions if p != position}
    visible = others.copy()

    for other in others:
        delta = vector_shorten(vector_subtract(other, position))

        for i in itertools.count(start=1):
            obstructed = vector_add(other, vector_multiply(delta, i))

            if not within_bounds(obstructed, size):
                break

            visible.discard(obstructed)

    return len(visible)


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