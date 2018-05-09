import numpy as np

names = np.loadtxt("p042_words.txt", delimiter=',', dtype=str)

for ii in range(len(names)):
  i1 = names[ii].find("\"")
  i2 = names[ii].find("\'")
  names[ii] = names[ii][(i1+1):(i2-3)]


dic = {"A":1,"B":2, "C":3, "D":4, \
"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}

trinums = np.zeros(500)

for nn in range(1,501):
  trinums[nn-1] = 1/2 * nn * (nn+1)


count = 0
for ii in range(0, len(names)):
  s = names[ii]
  score = 0

  for jj in range(len(s)):
    score += dic[s[jj]]

  
  if(score in trinums):
    count += 1

print(count)
