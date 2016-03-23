#!/usr/bin/env python3

def is_odd(number):
    return number%2==1

def is_even(number):
    return number%2==0

def is_mult_of_four(number):
    return number%4==0

def is_mult_of_x(number, divisor):
    return number % divisor == 0

def both_ends(s):
    if len(s) < 2:
        string = ""
    else:
        string = (s[0:2] + s[-2:])
    return string

