#!/usr/bin/python

import fileinput

def calculate_fuel(mass):
    fuel = mass//3 - 2
    return 0 if fuel <= 0 else fuel + calculate_fuel(fuel)

fuel = 0
for mass in fileinput.input():
    fuel = fuel + calculate_fuel(int(mass))
print(fuel)
