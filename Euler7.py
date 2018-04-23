import numpy as np
import time as time

def sieve():
  N = 10**6

  num = set(range(2,N))

  tick = time.time()

  for ii in range(2, int(np.sqrt(N)) + 1):
    for jj in range(2*ii, N, ii):
      num.discard(jj)

  fin = sorted(num)

  tock = time.time()
  timediff = tock - tick

  print("Generated", len(fin), "primes in", timediff, "seconds")

  print(fin[10000])

sieve()
