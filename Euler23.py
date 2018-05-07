import numpy as np
from math import sqrt
from functools import reduce

def factors(n):
  step = 2 if n%2 else 1
  return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n%i == 0)))

abundant = []

top = 28123

for ii in range(12, top):
  facs = factors(ii)
  facs.remove(ii)
  add = sum(facs)
  if(add > ii):
    abundant.append(ii)

print(len(abundant))

issum = [False] * (top+1)

for ii in range(0, len(abundant)):
  for jj in range(ii, len(abundant)):
    if(abundant[ii] + abundant[jj] < top):
      issum[abundant[ii] + abundant[jj]] = True
    else: break

add = 0
for ii in range(0, top):
  if(issum[ii] == False):
    add += ii

print(add)

    
