#!/usr/bin/env python

import random

a = []

n = input("indicate length of list: ")

i = 0
while i < n:
    a.append(random.randrange(10000))
    i += 1

print a

j = 0
while j < len(a):
    # find the position of the smallest number in a[j:len(a)]
    # swap this number with the number at the jth position
    
    p = j
    k = j + 1
    while k < len(a):
        if a[k] < a[p]:
            p = k

        k += 1

    a[j], a[p] = a[p], a[j] 


    j += 1

print "\033[1;32;40mthe highest number is:", a[-1]
print "\033[1;33;40mthe lowest number is:", a[0], "thank you for using,\
 classicreviveme <3"

