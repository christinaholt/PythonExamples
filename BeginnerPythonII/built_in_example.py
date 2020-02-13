''' Some examples of Python built-in functions. '''

# Useful string functions
s = 'Oh, hello!   \n'

print(s)
print(s.rstrip())


# Useful container functions

x = list(range(4, 9))

for func in [len, reversed, sum, max, min]:
    print(f"{func.__name__} {func(x)}")

y = [0 for i in range(5)]
z = list(range(132, 137))

print(f"y is {y}")
print(f'any(y): {any(y)}')
print(f'all(y): {all(y)}')
y[1] = 1
print(f"y is {y}")
print(f'any(y): {any(y)}')
print(f'all(y): {all(y)}')


print(f"Zipping x, y, and z: {list(zip(x, y, z))}")


# Functions for inspecting objects
type(x)               # <class 'list'>
isinstance(x, str)    # False
id(x)                 # Unique number for the object x




