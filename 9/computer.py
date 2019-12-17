import math
from collections import defaultdict
from typing import List, Tuple, DefaultDict

Parameter = Tuple[int, int]
Memory = DefaultDict[int, int]
Program = Tuple[int, Memory]


def parse_program(source: str) -> Program:
    values = source.split(',')
    program = ((i, int(x)) for i, x in enumerate(values))
    memory = defaultdict(lambda: 0, program)
    return len(values), memory


def run_generator(program: Program):
    length, memory = program
    relative_base = 0
    ip = 0

    while ip < length:
        opcode, params, ip = read_instruction(memory, ip)

        def get_param(i):
            return get_parameter_value(memory, relative_base, params[i])

        def get_address(i):
            return get_parameter_address(relative_base, params[i])

        try:
            if opcode == 1:
                a, b, out = get_param(0), get_param(1), get_address(2)
                memory[out] = a + b

            elif opcode == 2:
                a, b, out = get_param(0), get_param(1), get_address(2)
                memory[out] = a * b

            elif opcode == 3:
                out = get_address(0)
                memory[out] = yield

            elif opcode == 4:
                value = get_param(0)
                yield value

            elif opcode == 5:
                value, next = get_param(0), get_param(1)

                if value != 0:
                    ip = next

            elif opcode == 6:
                value, next = get_param(0), get_param(1)

                if value == 0:
                    ip = next

            elif opcode == 7:
                a, b, out = get_param(0), get_param(1), get_address(2)
                memory[out] = 1 if a < b else 0

            elif opcode == 8:
                a, b, out = get_param(0), get_param(1), get_address(2)
                memory[out] = 1 if a == b else 0

            elif opcode == 9:
                a = get_param(0)
                relative_base += a

            elif opcode == 99:
                return

            else:
                raise Exception(f'Invalid opcode: {opcode}')

        except Exception as err:
            raise Exception(f'Instruction failed ({err}): {opcode}, {params}, {ip}')

    raise Exception('Program did not halt')


def run_list(program: Program, input: List[int]) -> List[int]:
    instance = run_generator(program)
    output = []

    try:
        value = next(instance)

        while True:
            if value is None:
                value = instance.send(input.pop(0))
            else:
                output.append(value)
                value = next(instance)
    except StopIteration:
        pass

    return output


def get_parameter_value(memory: Memory, relative_base: int, parameter: Parameter) -> int:
    mode, value = parameter

    if mode in (0, 2):
        address = get_parameter_address(relative_base, parameter)
        return memory[address]
    elif mode == 1:
        return value
    else:
        raise Exception(f'Invalid mode: {mode}')


def get_parameter_address(relative_base: int, parameter: Parameter) -> int:
    mode, value = parameter

    if mode == 0:
        return value
    if mode == 2:
        return value + relative_base
    else:
        raise Exception('Mode is not 0')


def get_opcode(instruction: int):
    return instruction % 100


def get_opcode_modes(instruction: int, count: int):
    return [
        math.floor((instruction % (10 ** (3 + i))) / (10 ** (2 + i)))
        for i in range(count)
    ]


param_counts = {
    1: 3,
    2: 3,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 3,
    8: 3,
    9: 1,
    99: 0,
}


def read_instruction(memory: Memory, ip: int) -> Tuple[int, List[Parameter], int]:
    opcode = get_opcode(memory[ip])
    count = param_counts[opcode]
    modes = get_opcode_modes(memory[ip], count)
    params = [(modes[i], memory[ip + i + 1]) for i in range(count)]
    return opcode, params, ip + count + 1
