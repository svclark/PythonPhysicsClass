import numpy as np

def count(n):
  n = int(n)
  sn = str(n)
  plus = 0

  for ii in range(len(sn)):
    plus += int(sn[ii])

  print("The sum of the digits is: ", plus)

  return

count(2**1000)
