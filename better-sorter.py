#!/usr/bin/env python


if __name__ == "__main__":
    a = [1, 2, 54, 32, 86, 9, 19, 24]

print a
i = 0
while i < len(a):
    p = i
    j = i + 1
    while j < len(a):
        if a[j] < a[p]:
            p = j
        j += 1

    a[i], a[p] = a[p], a[i]
    # print a

    i += 1

print a
