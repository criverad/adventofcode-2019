#!/usr/bin/env python3.7

import fileinput

class SpaceObject:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []
    
    def orbits(self, parent):
        parent.children.append(self)
        self.parent = parent

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
    
    def is_com(self):
        return self.parent is None

    def find_orbital_transfers(self, name, orb_transfers = 0, visited = set()):
        print("Exploring %s with %d transfers" % (self.name, orb_transfers))

        if (self.is_com()):
            return None

        if (self.name == name):
            print("Found %s with %d transfers" % (name, orb_transfers))
            return orb_transfers

        if (self.name in visited):
            print("%s has already been visited" % self.name)
            return None

        visited.add(self.name) # visit it

        print('Exploring children of ' + self.name)
        for c in self.children:
            t = c.find_orbital_transfers(name, orb_transfers + 1, visited)
            if (t is not None):
                print("%d Transfers found under %s" % (t, self.name))
                return t

        return self.parent.find_orbital_transfers(name, orb_transfers + 1, visited)

def parse_space_objects():
    com = None
    objects = {}
    for line in fileinput.input():
    # for line in lines:
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
print(transfers - 2)
