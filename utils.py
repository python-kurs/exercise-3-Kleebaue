# utility functions

# Use this file for all functions you create and might want to reuse later.
# Import them in the `main.py` script

# ---------

# Counts the occurences of each item in a text file
def count(listtocount):
    [[y,listtocount.count(y)] for y in set(listtocount)]
    return(dict((y,listtocount.count(y)) for y in set(listtocount)))
