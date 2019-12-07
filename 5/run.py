import sys

from computer import run

program = [int(x) for x in sys.stdin.readline().split(',')]
input = [int(x) for x in sys.argv[1:]]

output = run(program, input)

# print(program)
print(output)
