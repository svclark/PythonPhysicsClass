import numpy

def FactorialDigitSum(facnum):
  '''
  Project Euler Problem 20
  Function to find sum of the digits in a factorial
  '''
  fac = 1
  for i in range(facnum,1,-1):
    fac *= i
  string = str(fac)
  count = 0
  for i in range(0, len(string)):
    count += int(string[i])
  return count

def fib(n, computed = {0: 0, 1: 1}):
  if n not in computed:
    computed[n] = fib(n-1, computed) + fib(n-2, computed)
  return computed[n]

def fib_to(n):
  fibs = [0,1]
  for i in range(2, n+1):
    fibs.append(fibs[-1] + fibs[-2])
  return fibs

print("\nThe sum of all digits in 100! is:", FactorialDigitSum(100))
