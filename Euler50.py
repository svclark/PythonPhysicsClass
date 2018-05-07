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
lengths = []
limit = 1000

for ii in range(1, len(primes)):
  if(primes[ii] > limit): break

  else:
    this = primes[ii]
    print("\n\n\n",this)

    add = 0
    while (add < this):
      start = 0

      for jj in range(0, ii - start):
        index = start + jj

        print(primes[index])
        add += primes[index]

        if(add == this):
          lengths.append([this, index])
          break

        else: 
          continue
      start += 1

print(lengths)
      
