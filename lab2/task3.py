#3 Check if X is divisible by Y (do it in one line of code), print 'X is divisible by Y' or 'X is not divisible by Y'. (1p)
#Ad 3 Hint- use the "ternary operator" as we did calculating xIsEvenLog above.

X = 14; Y = 8
z3 = f"{X} is divisible by {Y}" if X%Y == 0 else f"{X} is not divisible by {Y}"
print(z3)