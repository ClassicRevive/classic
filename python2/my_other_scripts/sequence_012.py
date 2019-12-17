#!/usr/bin/env python


from time import sleep

i = 0
x = 0
nul = 0
one = 0
two = 0

while i < 50:
	x = (x + 1) % 3
	
	if x == 2:
		two += 1
	elif x == 1:
		one += 1 
	elif x == 0:
		nul += 1

	print x
	i += 1
	sleep(0.2)

print "null count:", nul
print "one count:", one
print "two count:", two
