import sys

WIDTH = 25
HEIGHT = 6
LAYER_SIZE = WIDTH * HEIGHT

image = [int(x) for x in sys.stdin.readline().strip()]
layers = [image[i:i+LAYER_SIZE] for i in range(0, len(image), LAYER_SIZE)]

result = []

for y in range(0, HEIGHT):
    for x in range(0, WIDTH):
        i = y * WIDTH + x
        pixels = (layer[i] for layer in layers)
        opaque = (pixel for pixel in pixels if pixel != 2)
        pixel = next(opaque, 2)
        result.append(pixel)

CHARACTERS = {
    1: '▓',
    0: ' ',
    2: '?',
}

for y in range(0, HEIGHT):
    for x in range(0, WIDTH):
        i = y * WIDTH + x
        print(CHARACTERS[result[i]], end='')

    print()
