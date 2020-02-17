#!/usr/bin/env python


def encode(cypher, s):
    encoded = ""
    
    i = 0
    while i < len(s):
        char = s[i]
        if char in cypher:
            encoded += cypher[char]
        else:
            encoded += char

        i += 1

    return encoded

if __name__ == "__main__":
    # building test cypher dictionaries
    plus_one_cypher = {}
    caesar_cypher = {}

    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

    # load lowercase letters into the encryption dictionary
    # caeserian encryption (up 13)
    # plus_one encrytion(up 1)

    i = 0
    while i < len(alphabet):
        letter = alphabet[i]
        if letter not in caesar_cypher:
            # load the letter and its upper case as well
            caesar_cypher[letter] = alphabet[i + 13]
            caesar_cypher[letter.upper()] = alphabet[i + 13].upper()

        i += 1
    

    for i in range(len(alphabet)-1):
        plus_one_cypher[alphabet[i]] = alphabet[i + 1]
        plus_one_cypher[alphabet[i].upper()] = alphabet[i + 1].upper()

    cypher_choice = raw_input("caeserian (a) or plus (b): ")
    message = raw_input("enter message to encrypt: ")

    if cypher_choice == "a":
        print encode(caesar_cypher, message)
    elif cypher_choice == "b":
        print encode(plus_one_cypher, message)
    else:
        print "invalid encryption (a or b!)"
    