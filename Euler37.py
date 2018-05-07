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
  n = 10**7
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
prime_sieve = primes2(n)
primes = list([str(p) for p in prime_sieve if not search('[024568]', str(p))])

#ncprimes = sum(all(pr in primes for pr in ltrunc(p)) for p in primes)
#ncprimes = [all(pr in primes for pr in ltrunc(p)) for p in primes]

tprimes = []
for ii in range(2, len(primes)):
  if(all(pr in primes for pr in ltrunc(primes[ii]))):
    if(all(pr in primes for pr in rtrunc(primes[ii]))):

      tprimes.append(int(primes[ii]))

#def is_prime(n):
  #for ii in range(2, int(n/2)):
    #if (n % ii == 0):
      #return False
      #break
    #elif (ii == int(n/2) - 1):
      #return True

#ls = tprimes[-1]
#sdp = [7,37,773,313,317,373,797]

"""
another = False
count = 0
while(another == False):
  
  for nn in sdp:
    new = int(str(ls) + str(nn))
    #print(new)

    if(all(is_prime(int(pr)) for pr in ltrunc(str(new)))):
      if(all(is_prime(int(pr)) for pr in rtrunc(str(new)))):

        tprimes.append(new)
        another = True


for nn in sdp:
  new = int(str(ls) + str(nn))
  if(is_prime(new) == True):
    tprimes.append(new)

for nn in sdp:
  new = int(str(nn) + str(ls))
  if(is_prime(new) == True):
    tprimes.append(new)

"""

print(len(tprimes))
print(tprimes)
print(sum(tprimes))

