#!/usr/bin/env python


import sys

codes = []

message = sys.stdin.read()

i = 0
while i < len(message):
    # parse each page first
    added = False
    pageno = 0
    while pageno < 10 and not(added):
        with open("page-" + str(pageno) + ".txt") as page:
            # within page we must parse lines and within lines characters
            # until code is added
            s = page.readlines()
            lineno = 0

            # may be wronge:
            while lineno < len(s) and not(added):
                # parse characrers in s[lineno]
                line = s[lineno]
                charno = 0
                while charno < len(line) and not(added):
                    # if character == message[i] and pageno, lineno, charno
                    # is not in codes list, append it to the list, otherwhise
                    # keep moving
                    cand_code = str(pageno)
                    cand_code += " " + str(lineno)
                    cand_code += " " + str(charno)
                    if line[charno] == message[i] and cand_code not in codes:
                        codes.append(cand_code)
                        added = True
                    charno += 1
                lineno += 1
        pageno += 1

    i += 1

i = 0
while i < len(codes):
    sys.stdout.write(codes[i] + "\n")
    with open("result-codes.txt", "a") as result:
        result.write(codes[i] + "\n")
    i += 1
