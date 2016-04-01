#!/usr/bin/env python3

from lab7_solution import (
        ducklings,
        count_letters,
        reverse_string,
        is_palindrome,
)

#from unittest import mock

# --------------------------------------------------------------------
# Unit Testing
#
# In this lab you will be writing unit tests for the programming
# problems from Lab 5. The solutions are provided in:
#
# lab7_solution.py
#
# The problem is that each of the solutions has an error in it. Your
# unit tests should find these errors.



# --------------------------------------------------------------------
# Problem 1
# 
# Fix ducklings' names
# 
# In Robert McCloskey’s book Make Way for Ducklings, the names of the
# ducklings are Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and
# Quack. This loop tries to output these names in order.
# 
# Of course, that’s not quite right because Ouack and Quack are
# misspelled. Can you fix it?
#

#def test_ducklings():
#    assert ducklings() == 

# --------------------------------------------------------------------
# Problem 2
# 
# Letter count
#
# Modify the count_letters function below so that:
#
# 1. It has two parameters: string and char
# 2. It implements the functionality specified in the comments
#
# Essentially, the function is returning the number of occurances of the
# parameter char in the parameter string.

def test_count_letters():
    inputs = [
            ("bob","b",2),
            ("shuttle","t",2),
            ("shuttle","u",1),
    ]

    for string, char, correct in inputs:
        assert count_letters(string, char) == correct

# --------------------------------------------------------------------
# Problem 3
#
# Reversing a string
# 
# Complete the following function such that it reverses the parameter
# string.

def test_reverse_string():
    assert reverse_string("chuckle") == "elkcuhc"
    assert reverse_string("jack") == "kcaj"

# --------------------------------------------------------------------
# Problem 4
# 
# Checking for palindromes
# 
# Complete the following such that it correctly determines whether the
# given parameter, string, is a palindrome
# 

def test_is_palindromes():
    assert is_palindrome("bob") == True
    assert is_palindrome("chuckle") == False
