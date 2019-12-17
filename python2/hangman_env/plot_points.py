#!/usr/bin/env python


import sys

points = {}

point_input = sys.stdin.readlines()

i = 0
while i < len(point_input):
    point = point_input[i].rstrip()
    # add points to dictionary
    points[point] = True

    i += 1


# insert plotting code

def generate_grid():
    y = 19
    x = 0

    while y > -1:
        # line = "|"
        grid = ["|"]
        x = 0
        while x < 20:

            coord = str(x) + " " + str(y)
            if coord in points:
                grid.append("*")
            else:
                grid.append(" ")

            x += 1
        # line += "|"
        # print line
        grid.append("|")
        new_grid = "".join(grid)
        print new_grid
        y -= 1

# print " " + "-" * 20

# generate_grid()

# print " " + "-" * 20
