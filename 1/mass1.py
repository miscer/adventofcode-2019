import math

with open('input.txt') as f:
  total = sum(math.floor(int(line) / 3) - 2 for line in f)
  print(total)