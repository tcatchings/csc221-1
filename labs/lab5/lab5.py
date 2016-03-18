# --------------------------------------------------------------------
# Problem 1
# 
# Fix ducklings' names
# Quack. This loop tries to output these names in order.
# 
# Of course, that’s not quite right because Ouack and Quack are
# misspelled. Can you fix it?

def ducklings():
    prefixes = "JKLMNOPQ"
    suffix = "ack"

    for letter in prefixes:
        if letter == "O" or letter == "Q":
            print(letter + "u" + suffix)
        else:
            print(letter + suffix)


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

def count_letters(string, char): # need two parameters here: string and char
    # initialize the variable count to zero
    count = 0
    for c in string:
        # if c is equal to char then,
        if c == char:
        #     add one to count
            count = count + 1
        pass  
    return count
    # return the count variable


# --------------------------------------------------------------------
# Problem 3
#
# Reversing a string
# 
# Complete the following function such that it reverses the parameter
# string.

def reverse_string(string):
    # initialize the variable rev_string to ''
    rev_string = ''
    # for each c in string 
    for c in string:
        # add c to the beginning of rev_string
        rev_string = c + rev_string 
    # return the rev_string variable
    return rev_string


# --------------------------------------------------------------------
# Problem 4
# 
# Checking for palindromes
# 
# Complete the following such that it correctly determines whether the
# given parameter, string, is a palindrome
# 

def is_palindrome(string):
    rev_string = reverse_string(string)
    if string == rev_string:
        return True 
    else:
        return False


# --------------------------------------------------------------------
# Problem 5
# 
# Create a new file with content
# 
# Create a new function named create_file that takes three parameters:
# 
# - filename (str): name of the file to create
# - content (str): data to put into the file
# - N (int): number of times to repeat the given content
#
# The function should create a new file with the the given filename
# and it should populate this file with the given content duplicated N
# times.

def create_file(filename, content, N):
    newFile = open(filename, "w")
    # write file with while loop
    while N > 0:
        N = N - 1
        newFile.write(content)
    newFile.close()


if __name__=='__main__':
    import lab5_test
    lab5_test.run()
