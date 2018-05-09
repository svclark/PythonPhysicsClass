import numpy as np
import time

def integer_right_triangles(top):
  top = int(top)
  cc = 0
  solcount = 0
  csol = []
  nsols = []

  tick = time.time()

  for ii in range(5, top+1):
    num = ii
    csol = []
    solcount = 0
  
    for aa in range(1, int(num/2)):
      for bb in range(aa, int(num/2)+1):
        #cc = np.sqrt(int(aa*aa) + int(bb*bb))
        #if(cc % 1 == 0):
        if(np.sqrt(int(aa*aa) + int(bb*bb)) % 1 == 0):
          cc = int(np.sqrt(int(aa*aa) + int(bb*bb)))
          if(cc not in csol and aa + bb + cc == num ):
            solcount += 1
            csol.append(cc)

    if(solcount >= 1):
      nsols.append([num, solcount])

  big = 0
  index = 0
  for ii in range(len(nsols)):
    if(nsols[ii][1] > big):
      big = nsols[ii][1]
      index = ii

  tock = time.time()
  dt = tock - tick

  print("This took",dt,"seconds")

  return nsols[index][0]

print("The number p less than or equal to 120 for which there is \
a maximum number of right triangles with integer sides and \
perimeter p is:", integer_right_triangles(1000))
