import numpy as np
import time as time

def recip(denom):
  
  dic_num = {}
  fin_num = {}

  tick = time.time()
  for kk in range(1,denom):
    res = 1
    for ll in range(1,denom):
      res = (10*res) % kk

      #if(ll < maxp): break

      if res == 1:
        dic_num[kk] = ll
        break
  
  fin_num = sorted(dic_num.items(), key=lambda x: x[1])
  tock = time.time()
  print("The longest period is (num:period)", fin_num[-1])
  print("Time: ", tock-tick, "s")

  return

recip(1000)

