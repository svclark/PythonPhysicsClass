import numpy as np


'''
M = 10000
pent = np.zeros(M)

for ii in range(1,M+1):
  pent[ii-1] = ii*(3*ii-1) / 2

diffs = []
for ii in range(0, len(pent)):
  for jj in range(len(pent)):

    if(pent[ii] + pent[jj] in pent and np.abs(pent[ii] - pent[jj]) in pent):

      diffs.append(np.abs(pent[ii] - pent[jj]))
'''

def findMinPent():

  diffs = set()
  n = 1000

  while True:

    n += 1
    s = n*(3*n-1) // 2

    for Pj in diffs:
      if(s-Pj in diffs and s-2*Pj in diffs):
        return s-2*Pj

    diffs.add(s)

#print(min(diffs))
print(findMinPent())
