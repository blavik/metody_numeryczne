#TASKS (4p)

#1 calculate & print the value of function y = 2x^2 + 2x + 2 for x=[56, 57, ... 100] (0.5p)

print("\nTask 1:")
y = lambda x: 2*x**2 + 2*x + 2
for i in range(56,101):
    print(f"y({i}) = {y(i)}")


#2 ask the user for a number and print its factorial (1p)

while True:
    try:
        x = input("\nTask 2:\nInsert the natural number: ")
        try: x = float(x)
        except: raise ValueError("Your input is not a number.")
        if (x % 1) != 0: raise ValueError("Your number is not of integer type.")
        x = int(x)
        if x < 0: raise ValueError("Your integer is less than 0.")
        y = 1
        for i in range(2,x+1):
            y *= i
        print(f"{x}! = ",y)
        break
    except ValueError as err: print("Error: ", err)


#3 write a function which takes an array of numbers as an input and finds the lowest value. Return the index of that element and its value (1p)

def f3(x):
    min = x[0]
    ind = 0
    for i in range(1,len(x)):
        if x[i] < min:
            min = x[i]
            ind = i
    return ind, min
x = [1, 3, -9, 5, 0, -0.2, 101, -20]
print("\nTask 3:\n(index, value) = ", f3(x))


#4 looking at lab1-input and lab1-plot files create your own python script that takes a number and returns any chart of a given length.
#the length of a chart is the input to your script. The output is a plot (it doesn't matter if it's a y=x or y=e^x+2x or y=|x| function, use your imagination)
#test your solution properly. Look how it behaves given different input values. (1p)

import numpy as np
import matplotlib.pyplot as plt

x = int(input("\nTask 4:\nInsert the natural number: "))
y = []
for i in range(x): y.append(i + 5 + np.random.randn())
plt.scatter(np.arange(1,x+1),y)
plt.title("Function f(x) = x + 5 with noisy data.")
plt.grid()
plt.show()


#5 upload the solution as a Github repository. I suggest creating a directory for the whole python course and subdirectories lab1, lab2 etc. (0.5p)
#Ad 5 Hint write in Google "how to create a github repo". There are plenty of tutorials explaining this matter.

print("\nDone.")
