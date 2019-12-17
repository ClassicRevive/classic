#!/usr/bin/env python

import random


a = [49, 32, 39, 13, 30, 12, 14, 19, 31, 31]
# k = 0
# while k < 20:
    # a.append(random.randint(1,100))
    # k += 1 

l = len(a) - 1
j = 0
print a 
while l > -1:
    while j < l:
        if a[j] > a[j + 1]:
            a[j], a[j +  1] = a[j + 1], a[j]
        # print a
        j += 1
    l -= 1
    j = 0

print a