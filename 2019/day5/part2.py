#!/usr/bin/env python3.7

import sys

POSITION = 0
IMMEDIATE = 1

def read_param(raw_input, idx, mode):
    return raw_input[raw_input[idx]] if mode == POSITION else raw_input[idx]

def intcode(raw_input, idx):
    print(raw_input)
    instr = str(raw_input[idx])
    opcode = int(instr[-2:])
    modes = [int(x) for x in instr[0:-2].rjust(3, '0')[::-1]] # right-justified + reversed
    print("instr:%s, opcode:%s, modes:%s" % (instr, opcode, modes))
    if (opcode == 99):
        return
    if (opcode == 1):
        rp1 = read_param(raw_input, idx + 1, modes[0])
        rp2 = read_param(raw_input, idx + 2, modes[1])
        wp = read_param(raw_input, idx + 3, IMMEDIATE)
        raw_input[wp] = rp1 + rp2
        intcode(raw_input, idx + 4)
    if (opcode == 2):
        rp1 = read_param(raw_input, idx + 1, modes[0])
        rp2 = read_param(raw_input, idx + 2, modes[1])
        wp = read_param(raw_input, idx + 3, IMMEDIATE)
        raw_input[wp] = rp1 * rp2
        intcode(raw_input, idx + 4)
    if (opcode == 3):
        wp = read_param(raw_input, idx + 1, IMMEDIATE)
        raw_input[wp] = int(input("Input(%d): " % (idx+1)))
        intcode(raw_input, idx + 2)
    if (opcode == 4):
        rp1 = read_param(raw_input, idx + 1, modes[0])
        print("Output: %d" % rp1)
        intcode(raw_input, idx + 2)
    if (opcode == 5): # jump-if-true
        rp1 = read_param(raw_input, idx + 1, modes[0])
        if (rp1 != 0):
            idx = read_param(raw_input, idx + 2, modes[1])
            intcode(raw_input, idx)
        else:
            intcode(raw_input, idx + 3)
    if (opcode == 6): # jump-if-false
        rp1 = read_param(raw_input, idx + 1, modes[0])
        print(rp1)
        if (rp1 == 0):
            idx = read_param(raw_input, idx + 2, modes[1])
            intcode(raw_input, idx)
        else:
            intcode(raw_input, idx + 3)
    if (opcode == 7): # less-than
        rp1 = read_param(raw_input, idx + 1, modes[0])
        rp2 = read_param(raw_input, idx + 2, modes[1])
        wp = read_param(raw_input, idx + 3, IMMEDIATE)
        raw_input[wp] = 1 if rp1 < rp2 else 0
        intcode(raw_input, idx + 4)
    if (opcode == 8): # equals
        rp1 = read_param(raw_input, idx + 1, modes[0])
        rp2 = read_param(raw_input, idx + 2, modes[1])
        wp = read_param(raw_input, idx + 3, IMMEDIATE)
        raw_input[wp] = 1 if rp1 == rp2 else 0
        intcode(raw_input, idx + 4)

# raw_input = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
# intcode(raw_input, 0)

filename = str(sys.argv[1])
with open(filename, 'r') as file:
    raw_input = [int(n) for n in file.read().split(',')]
    intcode(raw_input, 0)
