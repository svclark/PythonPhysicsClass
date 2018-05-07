import numpy as np
import time

def primetest(num):
    '''
    Checks if a number is prime
    '''
    arr = []
    num = int(num)
    isprime = False
    
    for ii in range(2, num):
        arr.append(num % ii)
    for i in range(0,len(arr)):
        if arr[i] == 0:
            isprime = False
            break
        else:
            isprime = True
    if(num == 2):
      isprime = True

    return isprime

def quadPrimes():

  tick = time.time()

  stuff = []
  maxn = 1000
  primes = []
  for i in range(2, maxn):
    if(primetest(i)): 
      primes.append(i)

  maxp = 0
  for aa in range(-1*maxn, maxn):
    for bb in range(0, len(primes)):
      if(aa < maxp and bb < maxp): break
      if(aa % 2 == 0): break

      pcount = 1
      for nn in range(0, np.absolute(primes[bb])+1):
        if(primetest(nn*nn + aa*nn + primes[bb])):
          pcount += 1
        else:
          if(pcount > maxp):
            stuff.append([aa,primes[bb],pcount])
          break

  maxindex = 0
  mv = 0
  for i in range(0, len(stuff)):
    if(stuff[i][2] > mv):
      mv = stuff[i][2]
      maxindex = i

  tock = time.time()

  print("This took:", tock-tick,"seconds")
  return stuff[maxindex][0] * stuff[maxindex][1]

print("\nBeggining the quadratic primes Euler problem. This takes about a minute so please be patient")
print("\nThe product of the coefficients that produce the most consecutive primes is: ", quadPrimes())
