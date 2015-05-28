import math

def findRoot(functie, a, b, epsilon):
    if math.fabs(b-a) <= epsilon:
        return 0.5*(a + b)
    else:
        m = 0.5*(b + a)
        onder = float(functie(a))
        midden = float(functie(m))
        if (onder > 0 and midden > 0) or (onder < 0 and midden < 0):
            c = findRoot(functie, m, b, epsilon)
            return c
        else:
            c = findRoot(functie, a, m, epsilon)
            return c