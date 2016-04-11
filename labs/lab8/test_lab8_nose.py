#!/usr/bin/env python3.4

from lab8 import (count_letters,
                  reverse_string,
                  is_palindrome,
                  match_ends,
                  front_x,
                  sort_last,)

def test_count_letters():
    assert count_letters('battle','t') == 2
    assert count_letters('abcd','d') == 1
    assert count_letters('john','t') == 0

def test_reverse_string():
    assert reverse_string('battle') == 'elttab'
    assert reverse_string('bob') == 'bob'
    assert reverse_string('b') == 'b'

def test_is_palindrome():
    assert is_palindrome('bob') == True
    assert is_palindrome('battle') == False

def test_match_ends():
    assert match_ends(['battle','bob','john','nothin']) == 2
    assert match_ends(['i','jack','lil','gag','yay']) == 3
    assert match_ends(['tristan','brandon','jack','jill']) == 0

def test_front_x():
    assert front_x(['mix','apple','xavier','xi']) == ['xavier','xi','apple','mix']
    assert front_x(['banana','apple','battle','jack']) == ['apple','banana','battle','jack']

def test_sort_last():
    assert sort_last([(1,7), (1,3), (3,4,5), (2,2)]) == [(2,2), (1,3), (3,4,5), (1,7)]
