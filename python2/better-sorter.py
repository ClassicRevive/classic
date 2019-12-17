#!/usr/bin/env python

import random



def random_list(n):
    a = []
    i = 0 
    while i < n:
        a.append(random.randrange(1000))
        i += 1

    return a


def sort_asc(a):
    i = 0
    while i < len(a):
        p = i
        j = i + 1
        while j < len(a):
            if a[j] < a[p]:
                p = j
            j += 1

        a[i], a[p] = a[p], a[i]
        # print a

        i += 1

    return a

def sort_desc(a):
    i = 0
    while i < len(a):
        p = i
        j = i + 1
        while j < len(a):
            if a[j] > a[p]:
                p = j
            j += 1

        a[i], a[p] = a[p], a[i]
        # print a

        i += 1

    return a
   

a = random_list(10)
print a
print sort_desc(a)
