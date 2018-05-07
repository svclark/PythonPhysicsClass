import numpy as np

def Spiral(size):
  '''
  Solving Euler Problem 28
  '''
  #First fill array up to square of number
  nums = np.zeros(size*size)
  for i in range(1, size*size+1):
    nums[i-1] = i
  
  diag = 0 #Running sum of diagonal elements
  skips = 0 #Amount to add to get numbers on diagonal
  index = 0 #Where to look in the array
  stop = False #Infinite loops are no fun
  ii = 0

  '''
  The loops below are doing all the work. They simply add numbers that are "skips" away four times. After adding four
  numbers, increment skips by 2. This is real fast and works for all n x n squares, where n is odd. It might work for n
  even, but that doesn't really make sense in our case
  '''
  while(stop == False):
    skips += 2
    ii = 0
    while(ii < 4):
      if(index > len(nums)): 
        stop = True
        break
      diag += nums[index]
      index += skips
      ii += 1
      

  return diag
print("\nThe sum of the diagonals in a 1001x1001 spiral is: ",Spiral(1001))

