import math

def combi(a, b):

    if b <= 0:
        return 0

    if a < b:
        return 0
    else:
        c = math.factorial(a)/math.factorial(b)*math.factorial(a-b)
    return c

print(combi(5,-2))  