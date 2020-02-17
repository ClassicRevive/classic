#!/usr/bin/env python

import random
import sys

# generate random integer list of n length
def random_list(n):
    a = []
    i = 0 
    while i < n:
        a.append(random.randrange(1000))
        i += 1

    return a

# boolean for ascending sort
def asc(a, b):
    return a < b

# boolean for descending sort
def desc(a, b):
    return b < a
    
# selection sort algorithim
def ssort(a, compare):
    i = 0
    while i < len(a):
        p = i
        j = i + 1
        while j < len(a):
            if compare(a[j], a[p]):
                p = j
            j += 1

        a[i], a[p] = a[p], a[i]
        # print a

        i += 1

    return a


try:
    arg = sys.argv[1]

    comparator = ""
    if arg == "-a":
        comparator = asc
    elif arg == "-d":
        comparator = desc

    n = int(sys.argv[2])
    a = random_list(n)
    
    print a
    print ssort(a, comparator)

except:
    print "illegal commandline arg (must be -a or -d then list length)"
    print "ex. xxx.py -a 20"

