#!/usr/bin/python

import sys

INITIAL_POINT = [0, 0]

class Section:
    def __init__(self, from_point, to_point):
        self.a = from_point
        self.b = to_point

    def is_horizontal(self):
        return self.a[1] == self.b[1]
    
    def is_vertical(self):
        return not self.is_horizontal()

    def points(self):
        if self.is_horizontal():
            step = 1 if self.a[0] <= self.b[0] else -1
            return set([(x, self.a[1]) for x in range(self.a[0], self.b[0] + step, step)])
        if self.is_vertical():
            step = 1 if self.a[1] <= self.b[1] else -1
            return set([(self.a[0], y) for y in range(self.a[1], self.b[1] + step, step)])

    def __str__(self):
        return "[%s -> %s]" % (self.a, self.b)

def manhattan_distance(point):
    [x, y] = point
    return abs(x) + abs(y)

def shortest_intersection(intersections):
    if intersections is None or len(intersections) == 0:
        return None
    return min([manhattan_distance(intersection) for intersection in intersections])

def next_point(point, instr):
    cmd = instr[0]
    num = int(instr[1:])
    [px, py] = point
    if cmd == 'L':
        return [px - num, py]
    elif cmd == 'R':
        return [px + num, py]
    elif cmd == 'U':
        return [px, py + num]
    elif cmd == 'D':
        return [px, py - num]

def as_points(paths):
    cur = INITIAL_POINT
    points = []
    for instr in paths:
        next = next_point(cur, instr)
        points.append(next)
        cur = next
    return points

def process_paths(wire_1_paths, wire_2_paths):
    wire_1_from = INITIAL_POINT
    intersections = set()
    for wire_1_to in as_points(wire_1_paths):
        wire_2_from = INITIAL_POINT
        section_1 = Section(wire_1_from, wire_1_to)
        section_1_points = section_1.points()
        for wire_2_to in as_points(wire_2_paths):
            section_2 = Section(wire_2_from, wire_2_to)
            section_2_points = section_2.points()
            print("s1: %s" % section_1)
            # print("s1 pts: %s" % section_1_points)
            print("s2: %s" % section_2)
            # print("s2 pts: %s" % section_2_points)
            points = section_1_points.intersection(section_2_points)
            if (points is not None and len(points) > 0):
                print("Intersections found: %s" % ",".join(map(str,points)))
                intersections = intersections.union(points)
            else:
                print("No intersections")
            wire_2_from = wire_2_to
        wire_1_from = wire_1_to
    return intersections

# wire1_path = ['R2','D2']
# wire1_path = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
# wire1_path = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
# wire2_path = ['D2','R3']
# wire2_path = ['U62','R66','U55','R34','D71','R55','D58','R83']
# wire2_path = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']
filename = sys.argv[1]
with open(filename, 'r') as file:
    lines = file.readlines()
    wire1_path = lines[0].replace('\n', '').split(',')
    wire2_path = lines[1].replace('\n', '').split(',')
    intersections = process_paths(wire1_path, wire2_path)
    print("all intersections: %s" % ",".join(map(str, intersections)))
    no_initial = [i for i in intersections if i[0] != 0 and i[1] != 0]
    print(",".join(map(str, no_initial)))
    shortest = shortest_intersection(no_initial)
    print(shortest)

# filename = sys.argv[1]
# with open(filename, 'r') as file:
#     lines = file.readlines()
#     wire1_path = lines[0].replace('\n', '').split(',')
#     wire2_path = lines[1].replace('\n', '').split(',')
#     intersections = process_paths(wire1_path, wire2_path)
#     shortest = shortest_intersection(intersections)
#     print(shortest)
