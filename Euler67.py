
striangle = []

f = open("p067_triangle.txt")

temp = []
for line in f.readlines():
  temp = line
  striangle.append(temp)

triangle = []
for i in range(0, len(striangle)):
  row = []
  newstr = ''

  for j in range(0, len(striangle[i])):
    if(striangle[i][j] == ' '): 
     row.append(int(newstr))
     newstr = ''

    #elif(striangle[i][j] == '\\' or striangle[i][j] == 'n'):
    elif(j == len(striangle[i]) - 1):
      row.append(int(newstr))
      newstr = ''
      break

    else:
      newstr += striangle[i][j]

  triangle.append(row)

rt = triangle[::-1]

big = 0
for ii in range(len(rt)-1):
  newrow = []
  for jj in range(len(rt[ii])-1):
    
    first = rt[ii][jj] + rt[ii+1][jj] 
    second = rt[ii][jj+1] + rt[ii+1][jj] 

    newrow.append(max(first, second))

  rt[ii+1] = newrow


print(rt[-1])
