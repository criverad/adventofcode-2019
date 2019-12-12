#!/usr/bin/env python3

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

def find_inputs(initial_state):
    i = 0
    while i < len(initial_state):
        j = 0
        while j < len(initial_state):
            print("Trying %d, %d" % (i, j))
            numbers = list(initial_state)
            numbers[1] = i
            numbers[2] = j
            intcode(numbers, 0)
            print("Result: %d" % numbers[0])
            if numbers[0] == 19690720:
                print("Found it!")
                return (i, j)
            j = j + 1
        i = i + 1

filename = str(sys.argv[1])
with open(filename, 'r') as file:
    initial_state = [int(n) for n in file.read().split(',')]
    (noun, verb) = find_inputs(initial_state)
    print("noun=%d, verb=%d" % (noun, verb))
    print("answer=%d" % (100*noun+verb))
