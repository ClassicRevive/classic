#!/usr/bin/env python

"""
n = input()

i = 0

while i < n:
    print i 
    i += 1

i = 0

while i < 10:
    print i + 1   # Do something 
    i += 1        # increase "i" value

# 2 ** i sequence using while loop

i = 0
while i < 10:
    print 2 ** i
    i += 1


# using total variable 

n = input()
i = 0
total = 0

while i < n:
    total = total + (i + 1)
    i += 1

print total
"""


total = 0

i = 0
while i < 10:
    n = input()
    total = total + n 
    i += 1

print total / 10
