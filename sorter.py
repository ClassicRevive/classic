#!/usr/bin/env python


import random


def random_input(n):
   a = []
   import random
   for i in range(n):
      a.append(random.randrange(1000))
   return a


def read_input():
   a = []
   line = raw_input()
   while line != "end":
      a.append(int(line))
      line = raw_input()
   return a


def sort(a):
    k = 0

    l = len(a) - 1
    j = 0

    while l > -1:
        while j < l:
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

            j += 1
        l -= 1
        j = 0

    return a

if __name__ == "__main__":
   import sys
   import getopt

   n = 0

try:
  opts, args = getopt.getopt(sys.argv[1:], "n:r:")
  for o, a in opts:
     try:
        if o == "-n":
           n = int(a)
        if o == "-r":
           n = int(a)
     except:
        print "not an integer:", a
        sys.exit(2)

except getopt.GetoptError as err:
  print str(err)
  sys.exit(2)

if 0 < n:
  a = random_input(n)
  import time
  start = time.time()
  sort(a)
  stop = time.time()
  duration = stop - start
  print int(1000 * duration), "(ms)"
else:
  a = read_input()
  sort(a)
  

