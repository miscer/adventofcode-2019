import itertools
import sys


def run(program):
    position = 0

    while program[position] != 99:
        opcode = program[position]

        if opcode == 1:
            [a, b, out] = program[position + 1:position + 4]
            program[out] = program[a] + program[b]
        elif opcode == 2:
            [a, b, out] = program[position + 1:position + 4]
            program[out] = program[a] * program[b]
        elif opcode == 99:
            return
        else:
            raise Exception('Invalid opcode: {}'.format(opcode))

        position += 4


program = [int(x) for x in sys.stdin.readline().split(',')]

for noun, verb in itertools.product(range(100), repeat=2):
    p = list(program)
    p[1] = noun
    p[2] = verb

    run(p)

    if p[0] == 19690720:
        print(100 * noun + verb)

