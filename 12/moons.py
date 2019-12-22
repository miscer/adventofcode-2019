import itertools

import numpy as np


class Moon:
    def __init__(self, position):
        self.position = np.array(position)
        self.velocity = np.array((0, 0, 0))

    def __repr__(self):
        return f'Moon({self.position}, {self.velocity})'

    def add_velocity(self, delta):
        self.velocity += delta

    def move_step(self):
        self.position += self.velocity


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


def simulate(moons, steps):
    print('Initial state:')

    for m in moons:
        print(m)

    print()

    for i in range(steps):
        simulate_step(moons)

        print(f'After {i + 1} steps:')

        for m in moons:
            print(m)

        print()


def total_energy(moons):
    return sum(sum(abs(m.position) * sum(abs(m.velocity))) for m in moons)


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

simulate(input_moons, 1000)
energy = total_energy(input_moons)
print(f'Total energy: {energy}')
