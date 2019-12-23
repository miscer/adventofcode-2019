import copy
import functools
import itertools
import math
import operator

import numpy as np


class Moon:
    def __init__(self, position):
        self.position = np.array(position)
        self.velocity = np.array((0, 0, 0))

    def __repr__(self):
        return f'Moon({self.position}, {self.velocity})'

    def __eq__(self, other):
        return (self.position == other.position).all() and (self.velocity == other.velocity).all()

    def add_velocity(self, delta):
        self.velocity += delta

    def move_step(self):
        self.position += self.velocity

    def coord_equal(self, other, i):
        return self.position[i] == other.position[i] and self.velocity[i] == other.velocity[i]


def apply_gravity(m1, m2):
    v1 = np.array((0, 0, 0))

    for i in range(3):
        if m1.position[i] < m2.position[i]:
            v1[i] = 1
        elif m1.position[i] > m2.position[i]:
            v1[i] = -1

    v2 = v1 * -1

    m1.add_velocity(v1)
    m2.add_velocity(v2)


def simulate_step(moons):
    for m1, m2 in itertools.combinations(moons, 2):
        apply_gravity(m1, m2)

    for m in moons:
        m.move_step()


def simulate(moons):
    reference = copy.deepcopy(moons)
    coord_steps = {}
    total_steps = 1

    simulate_step(moons)

    while len(coord_steps) < 3:
        for i in range(3):
            if all(m1.coord_equal(m2, i) for m1, m2 in zip(reference, moons)):
                coord_steps.setdefault(i, total_steps)

        simulate_step(moons)
        total_steps += 1

    return coord_steps


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


input_moons = [
    Moon((-19, -4, 2)),
    Moon((-9, 8, -16)),
    Moon((-4, 5, -11)),
    Moon((1, 9, -13))
]

test_moons = [
    Moon((-1, 0, 2)),
    Moon((2, -10, -7)),
    Moon((4, -8, 8)),
    Moon((3, 5, -1))
]

steps = simulate(input_moons)
steps_lcm = functools.reduce(lcm, steps.values())
print(f'{steps_lcm} steps')
