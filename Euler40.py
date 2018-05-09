
"""
dcount = 0
intcount = 0
sint = ""
n = 0
prod = 1

while dcount < 1000001:
#while dcount < 101:
  intcount += 1
  sint = str(intcount)

  dcount += len(sint)

  if(dcount >= 10**n):
    
    prod *= int(sint[dcount - 10**n - 1])
    print(10**n, int(sint[dcount - 10**n - 1]))

    n += 1


print(prod)
"""


#Try again using the dumb way

si = []
ic = 0
while(len(si) < 1000001):
#while(len(si) < 101):
  ic += 1
  s = str(ic)
  for i in range(0, len(s)):
    si.append(s[i])

p = 1
for n in range(0, 7):

  p *= int(si[(10**n) - 1])

#print(si[1-1], si[10-1], si[100-1])
print(p)

