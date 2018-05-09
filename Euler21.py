from math import sqrt
from functools import reduce

def factors(n):
  step = 2 if n%2 else 1
  return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n%i == 0)))

top = 10000
an = []
count = 0

for i in range(2, top):
  fsum = sum(factors(i))-i
  if(sum(factors(fsum)) - fsum == i and i not in an):
    if(i != fsum):
      an.append(i)
      an.append(fsum)

#print(factors(284))
#print(sum(factors(220)) - 220)
#print(sum(factors(284)) - 284)

print(count)
print(an)
print(sum(an))
