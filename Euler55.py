import numpy as np

def is_lychrel(num):

  lychrel = False

  for ii in range(0,51):
    rnum =  int(str(num)[::-1])
    add = num + rnum

    if(add == int(str(add)[::-1])):
      lychrel = True
      break

    num = add

  return lychrel

count = 0
for ii in range(10, 10000):
  
  if(is_lychrel(ii) == False):
    count += 1



print(count)

