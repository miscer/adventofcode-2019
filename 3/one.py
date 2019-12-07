import sys
from collections import defaultdict
from itertools import repeat


def parse_wire(line: str):
    parts = line.strip().split(',')

    return [
        (part[0:1], int(part[1:]))
        for part in parts
    ]

directions = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}

def get_positions(wire):
    x, y = 0, 0

    for direction, distance in wire:
        for _ in repeat(None, distance):
            yield x, y

            dx, dy = directions[direction]
            x, y = (x + dx, y + dy)

def trace_wire(wire):
    grid = defaultdict(lambda: False)

    for position in get_positions(wire):
        grid[position] = True

    return grid

def find_intersections(grid, wire):
    intersections = []

    for position in get_positions(wire):
        if grid[position] and position != (0, 0):
            intersections.append(position)

    return intersections

def manhattan_distance(a, b):
    x1, y1 = a
    x2, y2 = b

    return abs(x1 - x2) + abs(y1 - y2)

wire_a = parse_wire(sys.stdin.readline())
wire_b = parse_wire(sys.stdin.readline())

grid = trace_wire(wire_a)
intersections = find_intersections(grid, wire_b)
distances = [manhattan_distance((0, 0), a) for a in intersections]
shortest = min(distances)

print(shortest)
