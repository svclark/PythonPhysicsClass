import numpy as np

nums = np.zeros(100)
count = 0

for ii in range(0,10):
  for jj in range(0,10):

    s = str(ii) + str(jj)
    nums[count] = int(s)
    count += 1

denoms = nums
match = []

for ii in range(0, len(nums)):
  for jj in range(1, len(denoms)):

#for ii in range(49, 50):
  #for jj in range(98, 99):
    snum = str(nums[ii])
    sden = str(denoms[jj])

    i1 = snum.find(".")
    i2 = sden.find(".")
    snum = snum[0:(i1)]
    sden = sden[0:(i2)]

    first = nums[ii] / denoms[jj]

    for kk in range(0, len(snum)):

      if(snum[kk] in sden and len(snum) == 2 and len(sden) == 2):

        if(snum[1] != snum[0] and sden[0] != sden[1]):
          if(snum[1] != '0' and sden[1] != '0'):
            nsnum = snum.replace(snum[kk],"")
            nsden = sden.replace(snum[kk],"")


            newnum = int(nsnum)
            newden = int(nsden)

            if(newden != 0):
              new = newnum / newden


              if(new == first and new < 1):
                match.append([snum, sden, nsnum, nsden])

product = 1

for ii in range(0, len(match)):
  product *= int(match[ii][2]) / int(match[ii][3])
print("The decimal form of the answer is: ", product)
