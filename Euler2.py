#Project Euler Problem 2

def fibsum():
  fib = [1,1,2]
  add = 2
  newfib = 0
  maxval = 4000001
  while(newfib < maxval):
    loc = len(fib) - 1
    newfib = fib[loc] + fib[loc-1]
    if(newfib % 2 == 0):
      add += newfib
    fib.append(newfib)

  return add

print(fibsum())
