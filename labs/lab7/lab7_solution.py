
def ducklings():
    prefixes = "JKLMNOPQ"
    suffix = "ack"

    for letter in prefixes:
        if letter in {'O','Q','K'}:
            letter = letter + 'u'
        print(letter + suffix)


def count_letters(string, char):
    count = 0
    for c in string:
        if c==char:
            count += 1
    return count


def reverse_string(string):
    rev_string = ''
    for c in string:
        rev_string = c + rev_string 
    return rev_string


def is_palindrome(string):
    if reverse_string(string) == string:
        return True
    else:
        return False

