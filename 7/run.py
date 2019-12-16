import itertools
import sys

from computer import run


def get_phase_settings():
    return itertools.permutations(range(5, 10))


def parse_program():
    return [int(x) for x in sys.stdin.readline().split(',')]


def mock_run():
    setting = yield
    input1 = yield
    print(f'{setting}: got {input1}')
    yield input1 + 1
    input2 = yield
    print(f'{setting}: got {input2}')
    yield input2 + 1


def start_amplifier(setting, program):
    amplifier = run(program.copy())
    # amplifier = mock_run()

    assert next(amplifier) is None
    assert amplifier.send(setting) is None

    return amplifier


def get_next_output(amplifier, input):
    output = amplifier.send(input)
    assert output is not None

    try:
        assert next(amplifier) is None
        return output, True
    except StopIteration:
        return output, False


def run_amplifiers(settings, program):
    amplifiers = [start_amplifier(setting, program) for setting in settings]
    has_next = [None for _ in amplifiers]
    value = 0

    for i in itertools.cycle(range(len(amplifiers))):
        if has_next[i] is False:
            break

        value, has_next[i] = get_next_output(amplifiers[i], value)

    return value


program = parse_program()
# max_output = run_amplifiers((1,2,3,4,5), program)
max_output = max(run_amplifiers(settings, program) for settings in get_phase_settings())
print(max_output)
