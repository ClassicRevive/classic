#!/usr/bin/env python

import random
from time import sleep

a = []
n = input("choose a list length: ")
p = input("choose index to insert new number: ")
v = input("enter the number you would like to be inserted: ")


print "this is my take on the insert function which is built into python"
sleep(0.5)     

k = 0
while k < n:
    a.append(random.randint(0,100)) # create random len25 integer list
    k += 1

print a

i = 0
while i < len(a) + 1:
    if i == p:
        a.append("!!")  # if position p exists in list, append target
        # print a
        j = 1
        while a[p] != "!!":
            # swap "target" back until target pos is reached
            a[-j], a[-j - 1] = a[-j - 1], a[-j]  
            j += 1
            # print a
        a[p] = v  # assign v at the pos of "!!"
    i += 1

print a
