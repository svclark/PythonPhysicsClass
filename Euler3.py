import numpy as np
 
def sieve(maxn):
  '''
  Generates prime numbers
  '''
  a = [True] * maxn
  a[0] = a[1] = False

  for (i, isprime) in enumerate(a):
    if isprime:
      yield i
      for n in range(i*i, maxn, i):
        a[n] = False

  return a

def primefactor(num):
  '''
  Finds largest prime factor of num
  '''
  if(num > 10000):
    primelist = list(sieve(int(np.sqrt(num)) + 1))
  else:
    primelist = list(sieve(num))

  for i in range(0, len(primelist)):
    if (num % primelist[len(primelist) - i - 1] == 0):
      return primelist[len(primelist) - i - 1]
      break

print("The largest prime factor of 600851475143 is",primefactor(600851475143))
