import numpy as np
import time as time
from re import search


def primes2(n):
  multiples = set()
  prime = []

  for i in range(int(n/2), n+1):
    if i not in multiples:
      prime.append(i)
      multiples.update(set(range(i*i, n+1, i)))
  return prime

def sieve():
  n = 10**6
  num = set(range(2,n))

  tick = time.time()
  for ii in range(2, int(np.sqrt(n)) + 1):
    for jj in range(2*ii, n, ii):
      num.discard(jj)

  fin = sorted(num)

  tock = time.time()

  time_delta = float(tock - tick)

  print("Length of primes list: ", len(fin))
  print("It took exactly T={} s to generate {} prime numbers".format(time_delta,n))
  return fin

def rtrunc(s):
  return [s[:-n]  for n in range(1, len(s))]

def ltrunc(s):
  return [s[n:]  for n in range(1, len(s))]


n = 10000000
#prime_sieve = primes2(n)
prime_sieve = sieve()
primes = list([str(p) for p in prime_sieve if not search('[0468]', str(p))])

#ncprimes = sum(all(pr in primes for pr in ltrunc(p)) for p in primes)
#ncprimes = [all(pr in primes for pr in ltrunc(p)) for p in primes]

tprimes = []
for ii in range(2, len(primes)):
  if(all(pr in primes for pr in ltrunc(primes[ii]))):
    if(all(pr in primes for pr in rtrunc(primes[ii]))):

      if(int(primes[ii]) > 10):
        tprimes.append(int(primes[ii]))



print(len(tprimes))
print(tprimes)
print(sum(tprimes))

