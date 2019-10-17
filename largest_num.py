#!/usr/bin/env python
n = 10
i = 0
largest = input()

while i < n - 1:
    num = input()
    if largest < num:
        largest = num
    i += 1

print largest
