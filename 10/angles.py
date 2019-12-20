import math

directions = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]


def atan2(y, x):
    if y > 0:
        return -math.atan(x / y)
    elif y < 0 and x >= 0:
        return -math.pi - math.atan(x / y)
    elif y < 0 and x < 0:
        return math.pi - math.atan(x / y)
    elif y == 0 and x > 0:
        return -math.pi / 2
    elif y == 0 and x < 0:
        return math.pi / 2
    else:
        return None


for x, y in directions:
    angle = (atan2(y, x)) / math.pi
    print(f'[{x},{y}]: {angle}')