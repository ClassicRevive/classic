#!/usr/bin/env python3

import sys

def main():
    digits = "0123456789"

    for line in sys.stdin:
        line = line.split()
        base = int(line[1])
        number = line[0]

        decimal = 0
        for i in range(len(number)):
            decimal += (base ** i) * int(number[-1 - i])

        print(decimal)


if __name__ == '__main__':
    main()
