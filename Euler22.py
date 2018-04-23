import numpy as np

raw = np.loadtxt("names.txt", dtype=str, delimiter=",")
mylist = []


for i in range(0, len(raw)):
  index = raw[i].index("\"\'")
  mylist.append(raw[i][3:index])

mylist.sort()


dic = {"A":1,"B":2, "C":3, "D":4, \
"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}

current = 0
total = 0

for i in range(0, len(mylist)):
  current = 0
  thisString = mylist[i]

  for j in range(0, len(thisString)):
    current += dic[thisString[j]]
  
  current *= i+1

  total += current

print(total)

  
