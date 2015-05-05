import sys
import time
n = (sys.argv[1])
T1 = time.perf_counter()
N = int(n)
bestand = open(sys.argv[2], 'w')


count = 0
is_iets_nog_actief = [True] * (N + 2)
for i in list(range(2, N)):
    if is_iets_nog_actief[i]:
        count = count + 1
        bestand.write(str(i) + "\n")
        j = 2
        while j * i < N:
                is_iets_nog_actief[j * i] = False
                j += 1
bestand.close()
T2 = time.perf_counter()

print('Found ', str(count), 'Prime numbers smaller than', N, ' in', T2 - T1) 