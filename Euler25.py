import numpy as np

def fib_index(numdig):
  numdig = int(numdig)

  a = 1
  b = 1
  c = a+b
  index = 3

  while(len(str(c)) < numdig):
   a = b
   b = c
   c = a+b
   index += 1

  print(index)

fib_index(1000)
