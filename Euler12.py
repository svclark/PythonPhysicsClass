
import numpy as np
import sympy 
import time

done = False
numfacs = 500
triangle = 0
iterator = 1

t1 = time.time()

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
      if n % i:
        i += 1
      else:
        n //= i
    return n

def getNumFacs(num):
  n = largest_prime_factor(num)
  primelist = list(sympy.primerange(1,n+1))
  mults = np.zeros(len(primelist))
  
  for ii in range(len(primelist)-1,-1,-1):
    while(num % primelist[ii] == 0):
      num = num/primelist[ii]
      mults[ii] += 1
      if(num == 1): break


  numfacs = 1
  for ii in range(0, len(mults)):
    if(mults[ii] != 0):
      numfacs *= mults[ii] + 1

  return numfacs

while done == False:
  triangle += iterator
  iterator += 1

  if(getNumFacs(triangle) > numfacs):
    print(triangle)
    done=True

t2 = time.time()

print("This took", t2-t1, "seconds.")

