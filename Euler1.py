def multThreeFive():
  '''
  Function for finding the sum of all multiples of 3 or 5
  below 1000
  '''
  max = 1000
  add = 0
  for i in range(0, max):
    if (i % 3 == 0 or i % 5 == 0):
      add += i

  return add


print("The sum of all multiples or 3 or 5 below 1000 is", multThreeFive())

