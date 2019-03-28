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
    print(f"{X} is is divisible by {Y} and both are even")
else: print("Something's gone wrong :(")