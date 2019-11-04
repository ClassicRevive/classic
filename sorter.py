#!/usr/bin/env python
import random


a = []
k = 0
while k < 20:
    a.append(random.randint(1,100))
    k += 1 

l = len(a) - 1
j = 0

while l > -1:
    while j < l:
        if a[j] > a[j + 1]:
            a[j], a[j +  1] = a[j + 1], a[j]
        print a
        j += 1
    l -= 1
    j = 0

    
    