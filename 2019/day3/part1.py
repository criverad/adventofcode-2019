#!/usr/bin/python

import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Section:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def slope(self):
        return (b.y - a.y)/(b.x - a.x)
        
def manhattan_distance(point):
    return abs(point.x) + abs(point.y)

def shortest_intersection(intersections):
    if intersections is None:
        return None
    return min([manhattan_distance(intersection) for intersection in intersections])

def process_instr(instr, cur_point):
    cmd = instr[0]
    num = instr[1:]
    if cur_point == 'L':
        return Point(cur_point.x - num, cur_point.y)
    elif cur_point == 'R':
        return Point(cur_point.x + num, cur_point.y)
    elif cur_point == 'U':
        return Point(cur_point.x, cur_point.y + num)
    elif cur_point == 'D':
        return Point(cur_point.x, cur_point.y - num)

def intersection_point(section_1, section_2):
    # find out if they 1) intersect at some point in the two sections or 2) they are parallel on the same x or y

def process_paths(wire1_paths, wire2_paths):
    wire1_cur_point = Point(0,0)
    wire2_cur_point = Point(0,0)
    intersections = []
    for wire1_instr in wire1_paths:
        wire1_new_point = process_instr(wire1_instr, wire1_cur_point)
        for wire2_instr in wire2_paths:
            wire2_new_point = process_instr(wire2_instr, wire2_cur_point)
            point = intersection_point(
                Section(wire1_cur_point, wire1_new_point), 
                Section(wire2_cur_point, wire2_new_point))
            if (point is not None):
                intersections.append(point)

filename = sys.argv[1]
with open(filename, 'r') as file:
    lines = file.readlines()
    wire1_path = lines[0].replace('\n', '').split(',')
    wire2_path = lines[1].replace('\n', '').split(',')
    intersections = process_paths(wire1_path, wire2_path)
    shortest = shortest_intersection(intersections)
    print(shortest)
