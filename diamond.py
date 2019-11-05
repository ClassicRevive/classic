#!/usr/bin/env python

import sys
size = sys.argv[1]
size = int(size)

i = 1
odd = 1
while i < (int(size) / 2) + 1:
    print (" " * ((size / 2) - (i - 1)) + ("*" * odd))

    odd += 2
    i += 1


j = i
while j > 0:
    print (" " * ((size / 2) - (j - 1)) + ("*" * odd))

    odd -= 2
    j -= 1
