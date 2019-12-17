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

    def find_descendant(self, name):
        if (self.name == name):
            return self
        for c in self.children:
            o = c.find_descendant(name)
            if (o is not None):
                return o
        return None

    def find_orbital_transfers(self, name, orb_transfers = 0, visited = set()):
        if (self.name in visited):
            return None # object has already been visited
        visited.add(self.name) # visit it

        if (self.name == name):
            print('Found name ' + name)
            return orb_transfers

        transfers = []
        for c in self.children:
            print('Children of ' + self.name)
            t = c.find_orbital_transfers(name, orb_transfers + 1, visited)
            if (t is not None):
                transfers.append(t)

        if (len(transfers) > 0):
            return min(transfers)
        else:
            print('Parent of ' + self.name)
            return self.around.find_orbital_transfers(name, orb_transfers + 1, visited)

def parse_space_objects():
    com = None
    objects = {}
    # for line in fileinput.input():
    for line in lines:
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

lines = ['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L','K)YOU','I)SAN']
com = parse_space_objects()
com.display()
you = com.find_descendant('YOU')
print('&&&&&&&')
transfers = you.find_orbital_transfers('SAN')
print(transfers)
