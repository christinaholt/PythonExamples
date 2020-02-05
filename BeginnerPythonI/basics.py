#!/usr/bin/env python3
  
# This is a comment


# --- Import statements section.
import platform

# Print to the screen
print('Hello world.') # This is a comment

# Use an imported library.
version = platform.python_version()
print('This is python version {}.'.format(version))

# Python has 4 ways to format strings
n = 4
counter = 1
print('Python has %d ways of printing strings!' % n)
print('-' * 50)
print('%d. C Style Strings %s' % (counter, 'are being deprecated.')) # Python 2. Deprecated and removed in future versions

counter = counter + 1
print('{}. Python string object method with ".format()"'.format(counter)) # Use this with Python 3

counter = 3
print('{c}. Python string object with explicit declaration {mystr}'.format(c=counter, mystr=':)'))

counter += 1
print(f'{counter}. Python f-string, used in {min(float(version[:3]), 3.6)}+') # Python 3.6+
