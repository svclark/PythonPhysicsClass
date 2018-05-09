import numpy as np


top = 100
digcounts = 0

savem = []

for pp in range(1,top):
  for bb in range(1,top+2):

    exp = bb**pp
    sexp = str(exp)
    if len(sexp) == pp:
      digcounts += 1
      #savem.append([bb,pp,bb**pp])

print(digcounts)
#print(savem)


