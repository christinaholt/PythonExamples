#!/usr/bin/env python3

'''

This script provides examples of Python control structures.

'''




# If statement examples:
# --------------------------
condition = True
# condition = 2 > 45
# condition = 2 == '2'

if condition:
    print('The condition is true!')
elif not condition:
    print('The opposite of condition is true!')
else:
    print('The condition is false!')


# Other logical expressions
# --------------------------

n = '234'
inline = n.isnumeric()
print(f'Result of isnumric(n): {inline}')

inline = 'big' if int(n) > 20 else 'small'
print(f'Result of inline logic: {inline}')

# While loop example:
# --------------------------
n = 0
while(n <= 4):
    if n < 0:
        break
    if n == 2:
        continue
    print('counter: {i}'.format(i=n))
    n += 1
else:
    print("Reached end of counter loop")


# For loop examples:
# --------------------------
for i, animal in enumerate(['dog', 'duck', 'donkey']):
    print(f'List item {1}: {animal}')

tuples = [('dog', True), ('python', False), ('rock', True), ('raccoon', False)]
for animal, pet in tuples:
    neg = '' if pet else 'NOT '
    print(f'A {animal} is {neg}a pet')

for my_num in range(0, 36, 12):
    print(f'Printing a range: {my_num}')

# Types example
# --------------------------
types_list = [
    'bob',
    7,
    34.7,
    2 * 1.4,
    1 / 4,
    1 // 4,
    True,
    False,
    None,
    [1, 2, 4,],
    {'a': 2, 'b': 3}
]

for item in types_list:
    print(f'{item} is type: {type(item)}')
    if isinstance(item, dict):
        print(f'List item {item} is a Python Dictionary!')

my_dict = types_list[-1]


for key, value in my_dict.items():
    print(f'my_dict contents --- {key}: {value}')
