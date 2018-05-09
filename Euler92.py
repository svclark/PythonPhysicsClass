import numpy as np
import time

def chain(num):
  
  stuck = False

  while(num != 1 and num != 89):

    s = str(num)
    newnum = 0

    for ii in range(0, len(s)):

      newnum += int(s[ii]) ** 2

    num = newnum


  return num
  

top = 10000000
count = 0

ts = time.time()

for ii in range(1, top):
  if(chain(ii) == 89):
    count += 1

tf = time.time()

td = tf-ts

print("Time:", td)

print(count)
