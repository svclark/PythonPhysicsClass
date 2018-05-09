import math

count = 0
for nn in range(23,101):
  for rr in range(0, nn+1):

    c = math.factorial(nn) / ( math.factorial(rr) * math.factorial(nn-rr))

    if (c > 1000000): count += 1

print(count)
