import collections
import sys

import computer


COLOR_BLACK = 0
COLOR_WHITE = 1
DIRECTION_UP = 0
DIRECTION_RIGHT = 1
DIRECTION_DOWN = 2
DIRECTION_LEFT = 3
OUTPUT_LEFT = 0
OUTPUT_RIGHT = 1


def run_robot(program):
    panels = collections.defaultdict(lambda: COLOR_BLACK)
    direction = DIRECTION_UP
    position = (0, 0)

    robot = computer.run_generator(program)

    try:
        while True:
            assert next(robot) is None
            output_color = robot.send(panels[position])
            output_direction = next(robot)

            panels[position] = output_color

            if output_direction == OUTPUT_LEFT:
                direction = (direction + 3) % 4
            elif output_direction == OUTPUT_RIGHT:
                direction = (direction + 1) % 4

            x, y = position

            if direction == DIRECTION_UP:
                position = (x, y + 1)
            elif direction == DIRECTION_RIGHT:
                position = (x + 1, y)
            elif direction == DIRECTION_DOWN:
                position = (x, y - 1)
            elif direction == DIRECTION_LEFT:
                position = (x - 1, y)
    except StopIteration:
        pass

    return panels


program = computer.parse_program(sys.stdin.readline().strip())
result = run_robot(program)
print(len(result))