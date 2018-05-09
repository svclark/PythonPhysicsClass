import numpy as np
import time as time
#from Euler import prime_sieve
from re import search

L = 1000000

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
  #print("It took exactly T={} s to generate {} prime numbers".format(time_delta,n))
  return fin

def rotate(s):
  return [s[n:] + s[:n] for n in range(1, len(s))]

prime_sieve = sieve()

primes = set(['2','5'] + [str(p) for p in prime_sieve if not search('[024568]', str(p))])

ncprimes = sum(all(pr in primes for pr in rotate(p)) for p in primes)

print(ncprimes)

'''
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
  #print("It took exactly T={} s to generate {} prime numbers".format(time_delta,n))
  return fin
tstart = time.time()
primes = sieve()
cprimes = [2]
for ii in range(0,len(primes)):
  #if primes[ii] not in cprimes:
    sprime = str(primes[ii])
    if('2' not in sprime and '4' not in sprime and '6' not in sprime and '8' not in sprime and '0' not in sprime):
      l = len(sprime)
      if(l == 1):
        cprimes.append(int(sprime))
        continue
      else:
        news = ''
        for jj in range(0, l):
          news = sprime[1:] + sprime[:1]
          if(int(news) not in primes): break
          elif(jj == (l-1)):
            cprimes.append(int(sprime))
tfinish = time.time()
td = tfinish - tstart
#print(cprimes)
print(len(cprimes))
print("This took", td, "seconds")
'''
