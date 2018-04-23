import numpy as np

def gcd(a,b):
  a = int(a)
  b = int(b)
  c = min(a,b)

  arr = []

  for kk in range(1, c+1):
    if(a % kk == 0 and b % kk == 0):
      arr.append(kk)

  return arr[-1]

def lcm(a, b):
  a = int(a)
  b = int(b)

  res = a*b / gcd(a,b)

  return res

def main():
   N = 50
   arr = np.arange(1, N+1)

   res = np.long(1)

   for kk in range(0, len(arr)):
     res = lcm(arr[kk], res)

   print("The result is:", np.long(res))

main()
