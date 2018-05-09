
import numpy as np

total = np.long(0)
lim = 1000

for ii in range(1, lim):
  total += ii**ii

st = str(total)

print(st[-10:])
