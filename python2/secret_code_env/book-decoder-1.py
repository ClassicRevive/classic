#!/usr/bin/env python


from time import sleep
import sys

s = sys.stdin.readline()
message = ""

while 0 < len(s):
    # split up the input
    s = s.split()
    # print s
    page = s[0]
    line = int(s[1])
    char = int(s[2])

    # first, open the file in current dir named
    # page-(page).txt
    
    with open("page-" + page + ".txt", "r") as page_no:
        # now read the line'th line
        s = page_no.readlines()
        lineno = 0
        while lineno < len(s) and lineno < line:
            lineno += 1

        # once the line number is found, we must now add the char
        # at the char index to the message

        message += s[lineno][char]

    s = sys.stdin.readline()

print "GENERATING..."
sleep(1)
i = 0
while i < len(message):
    print message[i]
    sleep(1)
    i += 1
print message,
