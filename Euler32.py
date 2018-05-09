import numpy as np

def isPandigital(s):
  '''
  Checks if a string is pandigital
  '''
  if(sorted(s) == ['1','2','3','4','5','6','7','8','9']):
    return True
  else:
    return False
  
def Pandigital():
  #Solution to project euler problem 32
  
  parray = [] #Array of products with their multipliers
  for ii in range(1,1000):
    for jj in range(10,10000):
      if(ii*jj < 10000): #only want 4 digit products
        parray.append([ii,jj,ii*jj])


  allnums = [] #Will hold only the pandigital products
  s = "0"
  for ii in range(len(parray)):
    #Creates a string of multiplicand/multiplier/product
    s = str(parray[ii][0]) + str(parray[ii][1]) + str(parray[ii][2])
    #Checks for pandigitalness
    if(isPandigital(s)): allnums.append([parray[ii][0], parray[ii][1], parray[ii][2]])

  #Array and loop below are to count each product only once
  onlyonce = []
  for i in range(len(allnums)):
    if(allnums[i][2] not in onlyonce):
      onlyonce.append(allnums[i][2])

  #Add em together
  total = sum(onlyonce)
  print("The sum of all products whose multiplicand/multipler/product is pandigital is:" ,total)
  return


Pandigital()
