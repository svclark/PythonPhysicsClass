import numpy as np
import time

t1 = time.time()

def collatz(n):
  count = 1
  while(n != 1):
    if(n % 2 == 0):
      n = n/2
    else:
      n = 3*n + 1
    count += 1

  return count

def getLong(top):
  #nterms = np.zeros((2,top))
  nterms = []

  for i in range(1,top):
    nterms.append((i,collatz(i)))

  big = 0 
  bn = 0
  for i in range(0,len(nterms)):
    if (nterms[i][1] > big) :
      bn = nterms[i][0]
      big = nterms[i][1]
  return bn

print(getLong(1000000))

t2 = time.time()
print(t2-t1)
