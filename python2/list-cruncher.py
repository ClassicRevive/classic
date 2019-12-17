#!/usr/bin/env python


a = []

# this code will take the minimum 10 values inputted,
# and create a list of them in order

s = raw_input()
i = 0
while s != "end":
    while i < 10:
        a.append(int(s))
        s = raw_input()
        i += 1
        # print i
    # at this point, the list has 10 elements
    # we append the 11th, sort and pop

    a.append(int(s))

    j = 1
    while j < len(a):
        v = a[j]
        p = j
        while 0 < p and v < a[p - 1]:
            a[p] = a[p - 1]
            
            p -= 1

        a[p] = v

        j += 1

    a.pop()
    # print a
    
    # take another input and work from line 20
    s = raw_input()

print a