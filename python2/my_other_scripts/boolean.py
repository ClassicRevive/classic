#!/usr/bin/env python


import random
from time import sleep


# month == 4 or month == 6 or month = 9 or month == 11
i = 0
true_count = 0
false_count = 0


for year in range(1, 2019):
	
	print '{}AD '.format(year),  year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
	
	if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
		true_count += 1
	else:
		false_count += 1
	

print 'Leap years since 0AD:', true_count 
print 'Non leap years:', false_count
