import numpy as np

tri = 3
#tris = np.zeros(2000)
tris = []

pent = 5
pents = []
hexa = 6

match = 0
#count = 286
count = 0
matches = [[0,0],[0,0]]

#while count < 2000:
mn = 285
mx = 100000
for count in range(285, mx):

  tri = count * (count+1) / 2
  tris.append(tri)

print("First loop done")

#count = 286
#count = 0
#while len(pents) < 500:
for count in range(166, mx):

  pent = count * (3*count-1) / 2
  pents.append(pent)
    #print(len(pents))

print("Second loop done")

gotIt = False
#count = 286
#count = 0
thenum = 0
#while (gotIt == False):
hexas = []
for count in range(144, mx):

  hexa = count * (2*count-1)
  hexas.append(hexa)

for ii in range(len(tris)):
  if (tris[ii] in hexas):
    if(tris[ii] in pents):
      thenum = tris[ii]


print(thenum)
