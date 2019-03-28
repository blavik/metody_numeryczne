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