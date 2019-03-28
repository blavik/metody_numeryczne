# TASKS (8p)- calculate & print:
#0 Use alternative way of reading inputs - using library (0.5p)
from cs50 import get_float
x = get_float("Insert the radius for the first circle: ")
y = get_float("And for the second one: ")

#1 Perimeter & field of circles with given radius X for the first circle & Y for the second one. (1p)
print(f"1st circle : perimeter = {2*3.14*x}, field = {3.14*x**2}")
print(f"2nd circle : perimeter = {2*3.14*y}, field = {3.14*y**2}")

#2 Find X & Y that satisfy: X is divisible by Y and both X & Y are even. (0.5p)
# X = n1*n2*...*nk * 2**o
# Y = n1*...*nj * 2**p
# N = {1,2,...,j,...,k) - indexes, j <= k
# n1,n2,...,nj,...,nk - divisors of the number Y and/or X, belongs to the set of prime numbers \ {2}, nj <= nk
# o, p - the number of times that 2 divides x1 and x2 respectively, belongs to the set of natural numbers \ {0}, p <= o
Nj = [3,5,7]
Nk = Nj + [13]
p = 1
o = p + 1
X, Y = 2**o, 2**p
for i in Nj: Y *= i
for i in Nk: X *= i
if X % 2 == 0 and Y % 2 == 0 and X % Y == 0:
    print(f"\n{X} is is divisible by {Y} and both are even")
else: print("\nSomething's gone wrong :(")

#3 Check if X is divisible by Y (do it in one line of code), print 'X is divisible by Y' or 'X is not divisible by Y'. (1p)
#Ad 3 Hint- use the "ternary operator" as we did calculating xIsEvenLog above.
X = 14; Y = 8
z3 = f"\n{X} is divisible by {Y}" if X%Y == 0 else f"\n{X} is not divisible by {Y}"
print(z3)

#4 Add rounding for the above x/y operation. Round to 2 decimal points. Hint: look up in Google "python limiting number of decimals". (1p)
x = 15; y = 2.05
print(f"\nx = {x}, y = {y}\nx / y = {x / y:.2f}")

#5 Look at lab2-plot.py and create your own script which takes a number as an input and plots the same 3D wave but with different characteristics
# it's totally up to your imagination how do you want to amend the figure according to the input number (1p)
a = float(input("\nInsert a number: "))
exec(open("lab2-plot.py").read())


#6 Test your code. Check various edge cases. In other words: does your program (1, 3, 4 & 5)work for all input values?
# In case of task 4  do not forget to round to different amount of decimals and see if it still works.(3 p)

while True:
    try:
        x = input("\nInsert the natural number: ")
        try: x = float(x)
        except: raise ValueError("Your input is not a number.")
        if (x % 1) != 0: raise ValueError("Your number is not of integer type.")
        x = int(x)
        if x < 0: raise ValueError("Your integer is less than 0.")
        print(x)
        break
    except ValueError as err: print("Error: ", err)
