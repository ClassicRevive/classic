#!/usr/bin/env python

import random

if __name__ == "__main__":
    a = []
    p = 0
    v = 8

    k = 0
    while k < 20:
        a.append(random.randint(0,100))
        k += 1

print a

i = 0
while i < len(a) + 1:
    if i == p:
        a.append(-0.5)
        print a
        j = 1
        while a[p] != -0.5:
            a[-j], a[-j - 1] = a[-j - 1], a[-j]
            j += 1
            print a
        a[p] = v
    i += 1

print a
