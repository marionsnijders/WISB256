import math
import sys

def findRoot(functie, a, b, epsilon):
    if math.fabs(b-a) <= epsilon:
        print(0.5*(a + b))
        sys.exit
    else:
        m = 0.5*(b + a)
        onder = float(functie(a))
        midden = float(functie(m))
        if (onder > 0 and midden > 0) or (onder < 0 and midden < 0):
            findRoot(functie, m, b, epsilon)
        else:
            findRoot(functie, a, m, epsilon)