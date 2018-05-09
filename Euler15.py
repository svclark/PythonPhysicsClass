import math

def binomial(n, k):
  
  k = min(n,k)

  coefficient = math.factorial(n+k) / (math.factorial(k) * math.factorial(n))

  return coefficient

print (binomial(20,20))
