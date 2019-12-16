import sys

LAYER_SIZE = 25 * 6

image = [int(x) for x in sys.stdin.readline().strip()]
layers = [image[i:i+LAYER_SIZE] for i in range(0, len(image), LAYER_SIZE)]

layer = min(layers, key=lambda l: l.count(0))
checksum = layer.count(1) * layer.count(2)

print(checksum)
