#!/usr/bin/env python


n = input()


i = 0
prev = 0
current = 1

while i < n:
    # Do something
    print "previous", prev, "current", current
 
    tmp = current
    current = prev + current
    prev = tmp

    # Increment i
    i += 1
