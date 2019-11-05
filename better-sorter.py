#!/usr/bin/env python

import random

a = []

def random_list(n):
    i = 0 
    while i < n:
        a.append(random.randrange(1000))
        i += 1

    return a



def sort_asc(x):
    print x

    i = 0
    while i < len(x):
        p = i
        j = i + 1
        while j < len(x):
            if x[j] < x[p]:
                p = j
            j += 1

        x[i], x[p] = x[p], x[i]
        # print a

        i += 1

    return x

def sort_desc(x):
    print x

    i = 0
    while i < len(x):
        p = i
        j = i + 1
        while j < len(x):
            if x[j] > x[p]:
                p = j
            j += 1

        x[i], x[p] = x[p], x[i]
        # print a

        i += 1

    return x
   

random_list(10)
print sort_desc(a)
