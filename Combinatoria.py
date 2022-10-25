import math

def combi(a, b):
    if (type(a) == str or type(b) == str):
        return TypeError

    if b <= 0:
        return 0

    if a < b:
        return 0
    else:
        c = math.factorial(a)/math.factorial(b)*math.factorial(a-b)
    return c

print(combi("a", "b"))  