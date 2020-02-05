#!/usr/bin/env python3

import control_structures
'''
This script provides examples of using functions in Python.


 - The *args concept allows for passing a list of arguments to a function, and for a function to accept a list of
   arguments of arbitary length.

 - The **kwargs concept is the same, except a dictionary is used to pass or accept an arbitrary number of key word
   arguments.

 - The if __main__ construct is used so that functions can be declared in any order, and so that the main function is
   only run by default when the script is run (not on import of a script).

'''

def rec_example(x):

    if x >= 1:
        print(x, end = " ")
        rec_example(x - 1)
        print(x, end = " ")


def main():

    '''
    This script calls a bunch of functions.
    '''

    print('The script is entering the main() function.')

    print(f'Calling the add function with 3 and 7: {simple_add(3, 7)}')

    mysum = simple_add(4, 9)

    print('Calling rec_example ---------')

    rec_example(mysum)

    print()

    add_everything(*[2, 4, 5])


    vals = dict(x = 7, y = 8, z = 2)
    print(f"Calling simple_add with dict {vals}: {simple_add(**vals)}")

def add_everything(*args):
    ''' Return the sum of all arguments '''
    print(args)
    x = sum(args)
    print(x)
    return x

def simple_add(x, y, z=0):
    return x + y


# Common python pattern for a more procedural setup:
if __name__ == '__main__':

    print(f'This script is being run from the command line')
    main()
