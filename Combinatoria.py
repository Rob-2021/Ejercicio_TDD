import math
# from math import comb

# comb = combinations([5, 3], 2)

# for i in list(comb):
#     print(i)

def combi(a, b):

    if a < b:
        return 0
    else:
        c = math.factorial(a)/math.factorial(b)*math.factorial(a-b)
    return c

print(combi(5,2))  