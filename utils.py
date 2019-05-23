# utility functions

# Use this file for all functions you create and might want to reuse later.
# Import them in the `main.py` script

# ---------

def count(listtocount):
    [[y,listtocount.count(y)] for y in set(listtocount)]
    print(dict((y,listtocount.count(y)) for y in set(listtocount)))
    