#!/usr/bin/env python3

import hw4_solution
# --------------------------------------------------------------------
# Problem 1
# 
# Create a function, is_odd, that takes a number and returns True if
# that number is odd.
# 
# Function: is_odd
# 
# parameters:
# - number
#
# returns: boolean

def test_is_odd():
    assert hw4_solution.is_odd(5) == True
    assert hw4_solution.is_odd(6) == False


# --------------------------------------------------------------------
# Problem 2
# 
# Create a function, is_even, that takes a number and returns True if
# that number is even. 
# 
# Function: is_even
# 
# parameters:
# - number
#
# returns: boolean

def test_is_even():
    assert hw4_solution.is_even(6) == True
    assert hw4_solution.is_even(7) == False


# --------------------------------------------------------------------
# Problem 3
# 
# Create a function, is_mult_of_four, that takes a number and returns
# True if that number is a multiple of four. 
# 
# Function: is_mult_of_four
# 
# parameters:
# - number
#
# returns: boolean

def test_is_mult_of_four():
    assert hw4_solution.is_mult_of_four(8) == True
    assert hw4_solution.is_mult_of_four(7) == False


# --------------------------------------------------------------------
# Problem 4
# 
# Create a function, is_mult_of_x, that takes a number and a divisor
# and returns True if that number is divisible by divisor
# 
# Function: is_mult_of_divisor
# 
# parameters:
# - number
# - divisor
#
# returns: boolean

def test_is_mult_of_x():
    assert hw4_solution.is_mult_of_x(10, 5) == True
    assert hw4_solution.is_mult_of_x(7, 6) == False


# --------------------------------------------------------------------
# Problem 5
# 
# Given a string s, return a string made of the first 2 and the last 2
# chars of the original string, so 'spring' yields 'spng'. However, if
# the string length is less than 2, return instead the empty string.
#
# Function: both_ends
#
# parameters:
# - s
#
# returns: string

def test_both_ends():
    assert hw4_solution.both_ends("spring") == "spng"
    assert hw4_solution.both_ends("b") == ""
