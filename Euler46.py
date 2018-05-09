import numpy as np
from collections import defaultdict
from itertools import count

factors = defaultdict(list)
gold = {}
primes = set()

#count = 3

for n in count(2):

  if factors[n]:
    for mm in factors.pop(n):
      factors[mm+n].append(mm)

    if n % 2:
      for kk in range(1, int((n/2)**0.5)+1):
        p = n - 2 * kk**2

        if p in primes:
          gold[n] = kk
          break

      if not n in gold:
        break

  else:
    factors[n*n].append(n)
    primes.add(n)


print(n)
