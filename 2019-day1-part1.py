#!/usr/bin/python

import sys

filename = sys.argv[1]
f = open(filename, 'r')
lines = f.readlines()
sum = 0
for line in lines:
    mass = float(line)
    fuel = int(mass / 3) - 2
    sum = sum + fuel
print(sum)
f.close()
