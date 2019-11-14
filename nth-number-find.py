#!usr/bin/env python


s = raw_input()
n = input("input the nth numbe to search for: ")

number = 0
i = 0
j = 0

while number < n:
    # find the first intance of a digit

    while i < len(s) and (s[i] < "0" or "9" < s[i]):
        i += 1

    # use j to parse until the end of digit
    j = i + 1

    while j < len(s) and "0" <= s[j] and s[j] <= "9":
        j += 1
    
    # assign num as slice of number from string
    num = s[i:j] 

    # continue parsing (if number i less than 2 in this case)
    i = j + 1

    number += 1

print num
