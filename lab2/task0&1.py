#0 Use alternative way of reading inputs - using library (0.5p)
from cs50 import get_float

x = get_float("Insert the radius for the first circle: ")
y = get_float("And for the second one: ")

#1 Perimeter & field of circles with given radius X for the first circle & Y for the second one. (1p)
print(f"1st circle : perimeter = {2*3.14*x}, field = {3.14*x**2}")
print(f"2nd circle : perimeter = {2*3.14*y}, field = {3.14*y**2}")