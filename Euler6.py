#Project Euler Problem 6

def SumSquareDiff():
  sumsq = 0
  ssum = 0
  sqsum = 0

  for i in range(1,101):
    sumsq += i*i
    ssum += i

  sqsum = ssum*ssum

  diff = sqsum - sumsq

  return diff

print(SumSquareDiff())

  
