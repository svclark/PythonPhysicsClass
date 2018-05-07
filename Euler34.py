import math

s = ''
digfac = []

for ii in range(3,int(1e7)):
  s = str(ii)
  add = 0
  for jj in range(0, len(s)):
    add += math.factorial(int(s[jj]))

  if(ii == add):
    digfac.append(add)

print(sum(digfac))
