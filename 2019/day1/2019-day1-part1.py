#!/usr/bin/python

import sys

filename = sys.argv[1]
with open(filename, 'r') as file:
    data = file.read().split(',')