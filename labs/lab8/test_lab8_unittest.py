#!/usr/bin/env python3.4

import unittest
from lab8 import (count_letters,
                  reverse_string,
                  is_palindrome,
                  match_ends,
                  front_x,
                  sort_last,)

class TestLab(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_count_letters(self):
        self.assertEqual( count_letters('battle','t'), 2)
        self.assertEqual( count_letters('abcd', 'd'), 1)
        self.assertEqual( count_letters('john', 't'), 0)

    def test_reverse_string(self):
        self.assertEqual( reverse_string('battle'), 'elttab')
        self.assertEqual( reverse_string('bob'), 'bob')
        self.assertEqual( reverse_string('b'), 'b')
        
    def test_is_palindrome(self):
        self.assertTrue( is_palindrome('bob') )
        self.assertFalse( is_palindrome('battle') )

    def test_match_ends(self):
        self.assertEqual( match_ends(['battle','bob','john','nothin']), 2)
        self.assertEqual( match_ends(['i','jack','lil','gag','yay']), 3)
        self.assertEqual( match_ends(['tristan','brandon','jack','jill']), 0)

    def test_front_x(self):
        self.assertEqual( front_x(['mix','apple','xavier','xi']), ['xavier','xi','apple','mix'])
        self.assertEqual( front_x(['banana','apple','battle','jack']), ['apple','banana','battle','jack'])

    def test_sort_last(self):
        self.assertEqual( sort_last([(1,7), (1,3), (3,4,5), (2,2)]), [(2,2), (1,3), (3,4,5), (1,7)])

if __name__ == "__main__":
    unittest.main()
