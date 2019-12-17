#!/usr/bin/env python

import sys
import random
import plot_points

# I want this program to take a word from list of words
# i want it to set this word as secret word
# I want 10 guesses and each guess is a character
# if character not in word then -1 guess
# if it is, then update dashes
# I am now trying to add a stickman system based on the point plot program
# previously written


# want the points to change based on guess numeber
def points(guesses):
    with open("stickman.txt") as stick:
        point_input = stick.readlines()
        i = 0
        while i < len(point_input) / (guesses + 1):
            point_input.pop()
            i += 1
        
        j = 0
        while j < len(point_input):
            point = point_input[j].rstrip()
            # add points to dictionary
            points[point] = True

            j += 1
    return points


words = [  # this method of making a list probably isnt most efficient..
""" 
Angel
Eyeball
Pizza
Angry
Fireworks
Pumpkin
Baby
Flower
Rainbow
Beard
Flying saucer
Recycle
Bible
Giraffe
Sand castle
Bikini
Glasses
Snowflake
Book
High heel
Stairs
Bucket
Ice cream cone
Starfish
Bumble bee
Igloo
Strawberry
Butterfly
Lady bug
Sun
Camera
Lamp
Tire
Cat
Lion
Toast
Church
Mailbox
Toothbrush
Crayon
Night
Toothpaste"""]


# create list of words 
words = words[0].split()
# decapitalize
# done in list and considering only first char to reduce big O 
for i in range(len(words)):
    char = words[i][0]
    if char.isupper():
        words[i] = words[i].lower()

try_again = 1 == 1

# system for updating dashes
def update_dashes(secret_word, dashes, guess):
    dash = ""
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            dash += guess
        else:
            dash += dashes[i]

    return dash




while try_again:
    # select a word to be the random word
    secret_word = words[random.randrange(len(words))]
    dashes = "-" * len(secret_word)

    guesses = 0
    while guesses < 10 and dashes != secret_word:
        print str(10 - guesses) + " guesses remaining"

        guess = raw_input("Input guess: ")

        if guess in secret_word and guess not in dashes:
            dashes = update_dashes(secret_word, dashes, guess)
            points = points(guesses)
            
            print " " + "-" * 20
            generate_grid()
            print " " + "-" * 20

            print dashes
        else:
            dashes = update_dashes(secret_word, dashes, guess)
            points = points(guesses)
            
            print " " + "-" * 20
            generate_grid()
            print " " + "-" * 20
            
            print dashes
            guesses += 1

    if dashes == secret_word:
        print "done! the word was:", secret_word
        try_again = 0 == 1
    else:
        print "Oof! the word was:", secret_word
        again = raw_input("try again? (y/n)  ")
        if again != y:
            try_again = 0 == 1

