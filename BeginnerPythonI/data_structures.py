#!/usr/bin/env python3


'''
This script provides some examples for using Python built-in structures.

The comment associated with each line should be the result obtained from that action.

Terms: 

    - mutable: may add, delete, change values
    - immutable: may NOT add, delete, change values

Useful Tidbits:
    - Python is zero-based
    - Unless you need to change items in a list, use a tuple
    - Use sets to compare membership.

'''


# Lists: mutable, [], ordered, sequential, iterable
# -----------------------------------------------------

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 2, 'rabbit', 5.8]
list3 = list(range(4))   # [0, 1, 2, 3]


# -- Referencing items in list
list1[2]  # 3
list2[3]  # 5.8
list2[-3] # 2

list2.index('rabbit')          # 2
list2.append('monkey')         # ['a', 2, 'rabbit', 5.8, 'monkey']
list2
list2.insert(1, 4)             # ['a', 4, 2, 'rabbit', 5.8, 'monkey']
list2

list2.extend(['joe', 'dan'])   # ['a', 4, 2, 'rabbit', 5.8, 'monkey', 'joe', 'dan']
list2
list2.remove('rabbit')         # ['a', 4, 2, 5.8, 'monkey', 'joe', 'dan']
list2
item = list2.pop()             # item = 'dan'; ['a', 4, 2, 5.8, 'monkey', 'joe']
list2
item
item = list2.pop(3)            # item = 5.8; ['a', 4, 2, 'monkey', 'joe']
list2
item
del list2[1]                   # ['a', 2, 'monkey', 'joe']
list2
del list2[1]
list2


# Print list with items separated by space
print(' '.join(list2))

# -- Re-assigning items in list
list1[2] = 44 #  [1, 2, 44, 4, 5]


# Tuples: immutable, ()
# -----------------------------
tup1 = ('tom', 'jill', 'dan')


# Dictionary: immutable, ()
# -----------------------------
fruits = {
    'apple': 'red',
    'banana': 'yellow',
    'orange': 'orange',
    }

veggies = dict(broccoli = 'green', tomato = 'fruit', squash = 'yellow')

veggies.keys()          # dict_keys(['broccoli', 'tomato', 'squash'])
veggies['broccoli']     # 'green'
veggies.get('cucumber') #



# Set: immutable, (), unordered
# -----------------------------

for i in set("Our future is bright"):
    print(i, end='')
print()



# Comprehnsion
# -----------------------------

# List comprehension takes the place of map/reduce
list2.extend([2, 4, 23.890])
list2 = [str(x) for x in list2]

# Create a dict with comprehension
food_colors = {color: fruit for fruit, color in fruits.items() }
food_length = {fruit: len(fruit) for fruit in fruits.keys() }


