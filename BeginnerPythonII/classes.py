#!/usr/bin/env python3

'''
Example of Python classes.

This script demonstrates the use of base classes, inheritance, and composition.

Inheritance implies "is a" relationship. Composition implies "has a" relationship.


'''


from abc import ABC, abstractmethod
import math



class Color:

    ''' Example of a base class. It doesn't have any parent classes, it's just an object.'''

    def __init__(self, name, hex_val):
        self.name = name
        self.hex_val = hex_val

    def __str__(self):
        return f"I'm the color {self.name}! Use my hex code: {self.hex_val}."


class Shape(ABC):

    ''' Example of an abstract class. This is a base class for specific shapes to build on. We want to ensure that a
    shape has certain methods and attributes defined every time, so we can define those here. '''

    # Note: 'type' is a special keyword in Python, add an underscore to give it a unique name
    def __init__(self, color):
        self.color = color

        # We only want to allow certain shapes. We don't know how to handle others.
        assert self.type_.lower() in ['circle', 'square', 'rectangle']

        # What is assert doing?
        # -------------------------------------------
        #if type_ in ['circle', 'square', 'rectangle']:
        #    self.type = type_
        #else:
        #    raise AssertionError
        #

    def __str__(self):
        ''' This is a special method that will (re)define how an object is printed.'''
        return f"Call me a {self.type_}. {self.color}"

    # We can use multiple decorators. This indicates that we must define a property in our derived/child classes.
    @property
    @abstractmethod
    def type_(self):
        ''' Meant to be a class variable for subclasses'''
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass



class Circle(Shape):

    ''' Circle (and the other shapes below) are subclasses (or child, or derived classes) that have an inheritance
    relationship with the Shape base class. In other words, a Circle "is a" Shape.'''

    type_ = 'Circle'

    def __init__(self, color, radius):
        # Tells python to set the "Shape" object variable color
        super(Circle, self).__init__(color)
        self.radius = radius

    def area(self):
        print(f'Computing pi*r^2')
        return math.pi * self.radius ** 2

    def perimeter(self):
        print(f'Computing 2*pi*r')
        return 2 * math.pi * self.radius


class Rectangle(Shape):

    ''' A Rectange "is a" Shape, so it inherits Shape.'''

    type_ = 'Rectangle'

    def __init__(self, color, length, width):
        super(Rectangle, self).__init__(color)

        self.length = length
        self.width = width

    def area(self):
        print(f'Computing rectangle area with sides {self.length}, {self.width}')
        return self.length * self.width

    def perimeter(self):
        print(f'Computing rectangle perimeter with sides {self.length}, {self.width}')
        return 2 * self.length + 2 * self.width


class Square(Rectangle, Shape):

    ''' A Square "is a" Shape, but it "is also a" special case of a Rectangle, so it inherits both.'''

    type_ = 'Square'

    def __init__(self, color, length):
        # Tells python to set the "Rectangle" object length and width to the same value, since it's a square
        super(Square, self).__init__(color, length, length)

if __name__ == '__main__':

    # The colors I use here come from the set of XKCD colors.

    # Create a color object from the Color class
    my_favorite_color = Color(name='teal blue', hex_val='#01889f')

    # Passing that color object to the Square class is an example of composition. Square "has a" color.
    square = Square(my_favorite_color, 4)

    print(square)

    # We can directly access the methods for each class
    print(f"My sides are all {square.length}, area: {square.area()}, perim: {square.perimeter()}")

    fun_color = Color(name='barney', hex_val='#ac1db8')
    circle = Circle(fun_color, 90)

    print(circle)
    print(f"My radius is {circle.radius}, area: {circle.area():.2f}, perim: {circle.perimeter():.2f}")
