"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    try:
        c = math.sqrt(a)
        if a < 0:
            raise ValueError
    except:
        print(ValueError)

    return c

def hypotenuse(a, b):
    c = math.hypot(a, b)
    return c

# First example
def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        c = b/a
        if a == 0:
            raise ZeroDivisionError
    except:
        print(ZeroDivisionError)


    return c


def log(a, b):
    try:
        c = math.log(b, a)
        if a <= 1 or b <= 0:
            raise ValueError
    except:
        print(ValueError)

    return c

def exp(a, b):

    return a**b
