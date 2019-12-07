import math

def fuel(mass):
  f = math.floor(mass / 3) - 2

  if f > 0:
    return f + fuel(f)
  else:
    return 0

with open('input.txt') as f:
  total = sum(fuel(int(line)) for line in f)
  print(total)