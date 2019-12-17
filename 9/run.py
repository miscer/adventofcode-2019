import sys

import computer

program = computer.parse_program(sys.stdin.readline().strip())
output = computer.run_list(program, [2])
print(output)

