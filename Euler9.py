import numpy as np
import time 

def pythag():
  '''
  Solving the pythagorean triplet euler problem
  '''
  ass = []
  bs = []
  cs = []
  val = 0
  tick = time.time()
  for a in range(50, 400):
    for b in range(50, 400):
      for c in range(100, 650):
        if(a*a + b*b == c*c):
          ass.append(a)
          bs.append(b)
          cs.append(c)
  tock = time.time()
  print("This took",tock-tick,"s to run")

  length = 0
  index = 0
  if (len(ass) != len(bs) or len(ass) != len(cs)):
    print("This ain't gonna work")
  else:
    length = len(ass)
    for i in range(0,length):
      if(ass[i] + bs[i] + cs[i] == 1000):
        index = i
    val = ass[index] * bs[index] * cs[index]

  return val

print("The product of abc for which a + b + c = 1000 and a^2 + b^2 = c^2 is (This takes about 30 seconds so be patient)")
print(pythag())
