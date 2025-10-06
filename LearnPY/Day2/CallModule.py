#Call Module
'''Modules in python are files that contain Python code,
which can include functions, classes and variables.
'''
#syntax
#import module

import math
print("Import Module Math")
print(math.pi)
print(math.sqrt(9))
print(math.floor(5.8))

# from module import 
from math import pi,factorial
print(pi)
print(factorial(5))

#import module as
from math import factorial as fact
print(fact(5))

import math as m
print(m.pi)

#import all function from module
from math import *
print(pi)
print(sqrt(9))
print(factorial(5))