#!/usr/bin/env python

import sys
arg = sys.argv[1]

i = 0
while i < len(arg) and arg[i] != "=":
    i += 1

header = arg[:i]
value = arg[i + 1:] 

s = raw_input()

# find position of search header in the first line 
index = 0
j = 0
k = 0
while index < 10:
    k = j
    while j < len(s) and s[j] != ",":
        j += 1


    target_header = s[k:j]
    
    if target_header == header:
        position = index

    j += 1
    index += 1

# print position

# search each line after for the value

s = raw_input()
while s != "end":
    j = 0
    k = 0
    
    index = 0
    while index < 10:
        k = j
        while j < len(s) and s[j] != ",":
            j += 1

        target_value = s[k:j]

        if target_value == value and index == position:
            print s

        j += 1
        index += 1

    s = raw_input()
