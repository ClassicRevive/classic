#!/usr/bin/env python3

'''convert base 10 number to any base <= 10'''

nnary = ""
base = int(input("input base: "))
n = int(input())

while n != 0:
    nnary = str(n % base) + nnary
    
    # print "n:", n
    # print "binary", binary
    n = n // base

print(nnary)
