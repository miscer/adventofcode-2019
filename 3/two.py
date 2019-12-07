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
    steps = 0

    for direction, distance in wire:
        for _ in repeat(None, distance):
            yield (x, y), steps

            dx, dy = directions[direction]
            x, y = (x + dx, y + dy)
            steps += 1

def trace_wire(wire):
    grid = {}

    for position, steps in get_positions(wire):
        grid.setdefault(position, steps)

    return grid

def find_intersections(grid, wire):
    intersections = []

    for position, steps in get_positions(wire):
        if position in grid and position != (0, 0):
            intersections.append(steps + grid[position])

    return intersections

wire_a = parse_wire(sys.stdin.readline())
wire_b = parse_wire(sys.stdin.readline())

grid = trace_wire(wire_a)
intersections = find_intersections(grid, wire_b)
shortest = min(intersections)

print(shortest)
