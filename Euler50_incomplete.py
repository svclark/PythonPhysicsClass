import numpy as np

def sieve():
  n = 10**6

  num = set(range(2,n))

  for ii in range(2, int(np.sqrt(n)) + 1):
    for jj in range(2*ii, n, ii):
      num.discard(jj)

  fin = sorted(num)


  return fin

primes = sieve()



print(lengths)
      
