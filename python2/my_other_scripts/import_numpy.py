#!/usr/bin/env python


print "Hello, welcome to my calculator program\nI made because I was extremely bored"

def arithmetic_calculator():
    op = raw_input("Input operator: ")
    num1 = input("Input number: ")
    num2 = input("Input another number: ")
    
    if op == "+":
        print "{} plus {} =".format(num1, num2), num1 + num2
    elif op == "-":
        print "the difference between {} and {} =".format(num1, num2), num1 - num2
    elif op == "*":
        print "{} multiplied by {} =".format(num1, num2), num1 * num2
    elif op == "/":
        print "{} divided by {} =".format(num1, num2), num1 / num2
    else:
        print "not a valid operator"


arithmetic_calculator()
