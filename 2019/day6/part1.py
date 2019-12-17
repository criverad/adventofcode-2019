#!/usr/bin/env python3.7

import fileinput

class SpaceObject:
    def __init__(self, name):
        self.name = name
        self.around = None
        self.children = []
    
    def orbits(self, around):
        around.children.append(self)
        self.around = around

    def display(self, indent = 0):
        indent_str = ''.ljust(indent, ' ')
        print(indent_str + self.name)
        for c in self.children:
            c.display(indent+1)
        return 

def parse_space_objects():
    com = None
    objects = {}
    for line in fileinput.input():
        [a, b] = line.strip().split(')')
        obj_a = objects.get(a)
        if obj_a is None:
            obj_a = SpaceObject(a)
            if (a == 'COM'):
                com = obj_a
            objects[a] = obj_a
        obj_b = objects.get(b)
        if obj_b is None:
            obj_b = SpaceObject(b)
            objects[b] = obj_b
        obj_b.orbits(obj_a)
    return com

def count_orbits(obj, cur_depth):
    return cur_depth + sum([count_orbits(o, cur_depth + 1) for o in obj.children])

com = parse_space_objects()
com.display()
print(count_orbits(com, 0))
