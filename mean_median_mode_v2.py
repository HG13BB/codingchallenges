import sys

import statistics

mainlist = '\n'.join(sys.stdin.readlines()).split()

#identical list with float
mainlist_f = [float(num) for num in mainlist]

#mean
mean = statistics.mean(mainlist_f[1:])

#median 
median = statistics.median(mainlist_f[1:])

#mode 
mode = int(min(statistics.multimode(mainlist_f[1:])))

#trim last decimal off of results for mean and median
result = [str(mean),str(median),str(mode)]

for i in result:
    print(i)
