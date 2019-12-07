import math
from typing import List, Tuple

Parameter = Tuple[int, int]


def run(program: List[int], input: List[int]):
    output = []
    ip = 0

    while ip < len(program):
        opcode, params, ip = read_instruction(program, ip)

        try:
            if opcode == 1:
                a = get_value(program, params[0])
                b = get_value(program, params[1])
                out = get_address(params[2])

                program[out] = a + b

            elif opcode == 2:
                a = get_value(program, params[0])
                b = get_value(program, params[1])
                out = get_address(params[2])

                program[out] = a * b

            elif opcode == 3:
                out = get_address(params[0])
                program[out] = input.pop(0)

            elif opcode == 4:
                value = get_value(program, params[0])
                output.append(value)

            elif opcode == 5:
                value = get_value(program, params[0])
                next = get_value(program, params[1])

                if value != 0:
                    ip = next

            elif opcode == 6:
                value = get_value(program, params[0])
                next = get_value(program, params[1])

                if value == 0:
                    ip = next

            elif opcode == 7:
                a = get_value(program, params[0])
                b = get_value(program, params[1])
                out = get_address(params[2])

                program[out] = 1 if a < b else 0

            elif opcode == 8:
                a = get_value(program, params[0])
                b = get_value(program, params[1])
                out = get_address(params[2])

                program[out] = 1 if a == b else 0

            elif opcode == 99:
                return output

            else:
                raise Exception(f'Invalid opcode: {opcode}')

        except Exception as err:
            raise Exception(f'Instruction failed ({err}): {opcode}, {params}, {ip}')

    raise Exception('Program did not halt')


def get_value(program: List[int], parameter: Parameter) -> int:
    mode, value = parameter

    if mode == 0:
        return program[value]
    elif mode == 1:
        return value
    else:
        raise Exception(f'Invalid mode: {mode}')


def get_address(parameter: Parameter) -> int:
    mode, value = parameter

    if mode != 0:
        raise Exception('Mode is not 0')

    return value


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
    99: 0,
}


def read_instruction(program: List[int], ip: int) -> Tuple[int, List[Parameter], int]:
    opcode = get_opcode(program[ip])
    count = param_counts[opcode]
    modes = get_opcode_modes(program[ip], count)
    params = [(modes[i], program[ip + i + 1]) for i in range(count)]
    return opcode, params, ip + count + 1
