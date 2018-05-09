#Project Euler Problem 10 
 
def sieve(maxn):
   bools = []
   primes = []
   for i in range(1, maxn):
     bools.append(True)
 
   for i in range(2, maxn):
     if bools[i - 2]:
       for j in range(i*2, maxn+1, i):
         bools[j - 2] = False
 
   for p in range(0, len(bools)):
     if (bools[p]):
       if(p + 2 < 1999999):
         primes.append(p+2)
       else:
         break
 
   return primes
 
def sumPrimes():
   primes = sieve(10000000)
   add = 0
   for i in range(0, len(primes)):
     add += primes[i]
 
   return add
 
 
print(sumPrimes())
