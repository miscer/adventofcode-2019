import itertools
import sys

from computer import run


def get_phase_settings():
    return itertools.permutations(range(5))


def parse_program():
    return [int(x) for x in sys.stdin.readline().split(',')]


def run_amplifiers(settings, program):
    value = 0

    for setting in settings:
        input = [setting, value]
        output = run(program, input)
        value = output[0]

    return value


program = parse_program()
max_output = max(run_amplifiers(settings, program.copy()) for settings in get_phase_settings())
print(max_output)
