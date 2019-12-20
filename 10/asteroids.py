import collections
import itertools
import math
import sys
from typing import Tuple, TextIO, Set, List, DefaultDict, Iterator

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


def vector_magnitude(vector: Vector) -> float:
    x, y = vector
    return math.sqrt(x ** 2 + y ** 2)


def atan2(y, x):
    if y > 0:
        return -math.atan(x / y)
    elif y < 0 and x >= 0:
        return -math.pi - math.atan(x / y)
    elif y < 0 and x < 0:
        return math.pi - math.atan(x / y)
    elif y == 0 and x > 0:
        return -math.pi / 2
    elif y == 0 and x < 0:
        return math.pi / 2
    else:
        return None


def polar_coordinates(point: Vector, reference: Vector) -> Tuple[float, float]:
    delta = vector_subtract(point, reference)
    distance = vector_magnitude(delta)
    direction = round(atan2(delta[1], delta[0]), 7)
    return distance, direction


def group_by_direction(map: Map, position: Vector) -> DefaultDict[float, Set[Tuple[Vector, float]]]:
    size, positions = map
    groups = collections.defaultdict(set)

    for other in positions:
        if other != position:
            distance, direction = polar_coordinates(other, position)
            groups[direction].add((other, distance))

    return groups


def count_visible_asteroids(map: Map, position: Vector) -> int:
    return len(group_by_direction(map, position))


def sort_by_laser(map: Map, position: Vector) -> Iterator[Vector]:
    groups = group_by_direction(map, position)

    while groups:
        for direction in sorted(groups.keys()):
            asteroids = groups[direction]
            closest = min(asteroids, key=lambda x: x[1])
            position, distance = closest
            yield position

            asteroids.remove(closest)

            if not asteroids:
                del groups[direction]


map = parse_map(sys.stdin)
size, positions = map

station_position = max(positions, key=lambda p: count_visible_asteroids(map, p))
print(station_position)

lasered = list(sort_by_laser(map, station_position))
nth = int(sys.argv[1])
print(lasered[nth - 1])
