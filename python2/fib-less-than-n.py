#!/usr/bin/env python


n = input()
prev = 0
current = 1

while prev < n:
    print prev

    tmp = current
    current = prev + current
    prev = tmp
