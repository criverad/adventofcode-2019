#!/usr/bin/env python3.7

import sys

POSITION = 0
IMMEDIATE = 1

def read_param(raw_input, idx, mode):
    return raw_input[raw_input[idx]] if mode == POSITION else raw_input[idx]

def intcode(raw_input, idx):
    # print(raw_input)
    instr = str(raw_input[idx])
    opcode = int(instr[-2:])
    modes = [int(x) for x in instr[0:-2].rjust(3, '0')[::-1]] # right-justified + reversed
    # print("instr:%s, opcode:%s, modes:%s" % (instr, opcode, modes))
    if (opcode == 99):
        return
    if (opcode == 1):
        rp1 = read_param(raw_input, idx + 1, modes[0])
        rp2 = read_param(raw_input, idx + 2, modes[1])
        wp = read_param(raw_input, idx + 3, IMMEDIATE) # write params are never in immediate mode
        raw_input[wp] = rp1 + rp2
        intcode(raw_input, idx + 4)
    if (opcode == 2):
        rp1 = read_param(raw_input, idx + 1, modes[0])
        rp2 = read_param(raw_input, idx + 2, modes[1])
        wp = read_param(raw_input, idx + 3, IMMEDIATE) # write params are never in immediate mode
        raw_input[wp] = rp1 * rp2
        intcode(raw_input, idx + 4)
    if (opcode == 3):
        wp = read_param(raw_input, idx + 1, IMMEDIATE) # write params are never in immediate mode
        raw_input[wp] = int(input("Input(%d): " % (idx+1)))
        intcode(raw_input, idx + 2)
    if (opcode == 4):
        rp1 = read_param(raw_input, idx + 1, modes[0])
        print("Output: %d" % rp1)
        intcode(raw_input, idx + 2)

# numbers = [3, 0, 4, 0, 99]
# numbers = [1002,4,3,4,33]
# intcode(numbers, 0)
# print(numbers)

filename = str(sys.argv[1])
with open(filename, 'r') as file:
    raw_input = [int(n) for n in file.read().split(',')]
    intcode(raw_input, 0)
    # print(raw_input)