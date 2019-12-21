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

    panels[position] = COLOR_WHITE
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


PRINT_COLORS = {
    COLOR_BLACK: '.',
    COLOR_WHITE: '#'
}


def print_panels(panels):
    min_x, max_x, min_y, max_y = 0, 0, 0, 0

    for position in panels.keys():
        x, y = position

        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y

    for y in range(max_y, min_y - 1, -1):
        for x in range(min_x, max_x + 1):
            color = panels[(x, y)]
            print(PRINT_COLORS[color], end='')
        print()


program = computer.parse_program(sys.stdin.readline().strip())
result = run_robot(program)
print_panels(result)
