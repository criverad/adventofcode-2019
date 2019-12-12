#!/usr/bin/env python2.7

import sys

def intcode(input, opcode):
    # print(input)
    # print(opcode)
    pos0 = input[opcode]
    if (pos0 == 99):
        return
    if (pos0 ==1 or pos0 == 2):
        if (pos0 == 1):
            input[input[opcode+3]] = input[input[opcode+1]] + input[input[opcode+2]]
        if (pos0 == 2):
            input[input[opcode+3]] = input[input[opcode+1]] * input[input[opcode+2]]
        intcode(input, opcode + 4)

filename = str(sys.argv[1])
with open(filename, 'r') as file:
    numbers = [int(n) for n in file.read().split(',')]
    numbers[1] = 12
    numbers[2] = 2
    intcode(numbers, 0)
    print(numbers)