import numpy as np

amin = 2
amax = 100
bmin = 2
bmax = 100

allnums = []

for aa in range(amin, amax+1):
  for bb in range(bmin, bmax+1):

    if(aa**bb not in allnums):
      allnums.append(aa**bb)

print(len(allnums))

