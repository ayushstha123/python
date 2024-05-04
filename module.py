import random as rdm #by using as we can make our own alias
# what is alias (shortform of modules)
import sys
from enum import Enum
# import math
from math import pi
import module_example

print(rdm.choice(str(432)))
print(f"{pi:.2f}")

print(module_example.capital)
module_example.randomFunFact()

print(__name__)
print(module_example.__name__)
