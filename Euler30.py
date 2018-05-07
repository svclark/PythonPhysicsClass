import numpy as np

def Other(numdig):
  '''
  Solution to euler 30.
  Too slow but works
  '''
  top = 10**(numdig + 1)

  snum = "poop"
  stuff = []
  num = 0
  for i in range(0, top):
   snum = str(i)
   num = 0
   for j in range(0, len(snum)):
     num = num + (int(snum[j])) ** numdig
   if(num == i): stuff.append(i)

  print("The sum of all numbers that can be written as a sum of thefifth power of their digits is: ", sum(stuff) - 1)
  
Other(5)
