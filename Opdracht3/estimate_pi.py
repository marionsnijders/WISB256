import random
import math
import sys
import time

if len(sys.argv) < 3:
    print('Use: estimate_pi.py N L')
    sys.exit()
    
N = float(sys.argv[1])
L = float(sys.argv[2])
count_true = 0

if len(sys.argv) == 4:
    random.seed(sys.argv[3])

if L > 1:
    print('AssertionError: L should be smaller than 1')
    sys.exit()
    
def drop_needle(L):
    x1 = random.random()
    hoek = random.vonmisesvariate(0,0)
    x2 = x1 + L * math.sin(hoek)
    if x2 > 1 or x2 < 0:
        return True
    else:
        return False
        
for i in range(0, int(N)):
    if drop_needle(L):
        count_true += 1
        
    
print(count_true, 'hits in', int(N), 'tries')
pi = 2 * L * N / count_true
print('Pi =', pi)