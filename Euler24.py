import numpy as np

def permute(vals, low=0):

  if(low + 1 >= len(vals)):
    yield vals
  
  else:
    for p in permute(vals, low+1):
      yield p

    for ii in range(low+1, len(vals)):
      vals[low], vals[ii] = vals[ii], vals[low]
      
      for p in permute(vals, low+1):
        yield p

      vals[low], vals[ii] = vals[ii], vals[low]

sallpermutes = []

arr = [0,1,2,3,4,5,6,7,8,9]
sarr = ['0','1','2','3','4','5','6','7','8','9']
for p in permute(arr):
  temp = str(p)
  sallpermutes.append(temp)

print("Got all permutations")

sperm = []
for ii in range(0, len(sallpermutes)):
  this = ''
  use = ''

  for jj in range(0, len(sallpermutes[ii])):
    
    this = str(sallpermutes[ii][jj])
    if(this in sarr):
      use += this
    else: continue

  sperm.append(use)

print("Got them all as strings")

iperm = np.zeros(len(sperm))
for ii in range(0, len(sperm)):
  iperm[ii] = int(sperm[ii])

print("Got them all as integers")

sort = sorted(iperm)

print(sort[1000000-1])
