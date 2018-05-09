import numpy as np

p1 = 1
p2 = 2
p5 = 5
p10 = 10
p50 = 50
e1 = 100
e2 = 200

#coins = [p1, p2, p5, p10, p50, e1, e2]
coins = [1,2,5,10,20,50,100, 200]

amount = 200

ways = [0] * (amount + 1)
ways[0] = 1

for coin in coins:
  for jj in range(coin, amount+1):
    ways[jj] += ways[jj-coin]

print(ways[amount])

