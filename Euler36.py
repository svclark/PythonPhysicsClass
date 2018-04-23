'''
Solution to Project Euler Problem 36
'''

import numpy as np

def palindrome_check(string):
  '''
  Checks if a string is a palindrome, returns true or false
  '''
  string = str(string)
  rstring = string[::-1]
  if(string == rstring): return True
  else: return False

def bin_to_dec(num):
  '''
  Convert a binary number to decimal
  '''
  num = int(num)
  snum = str(num)
  
  dec = 0
  last = len(snum) - 1

  for ii in range(0, len(snum)):
    if (snum[ii] == "1"): dec += 2**(last - ii)
    
  return dec

def dec_to_bin(num):
  '''
  convert a decimal number to binary
  '''
  num = int(num)
  snum = str(num)
  binary = ""

  quotient = 1
  remainder = 1
  while(quotient > 0):
    quotient = int(num / 2)
    remainder = num % 2
    num = quotient
    binary += str(remainder)
  
  bnum = int(binary[::-1])
  return bnum

def get_pals(big):
  '''
  Sums numbers that are palindromes in base 10 and base 2
  '''

  big = int(big)
  dnums = np.arange(1,big)
  psum = 0
  bnum = 0

  for ii in range(len(dnums)):
    if(palindrome_check(dnums[ii]) == True):
      bnum = dec_to_bin(dnums[ii])
      if(palindrome_check(bnum) == True):
        #print(dnums[ii], bnum)
        psum += dnums[ii]

  return psum


print("The sum of all numbers below one million that are palindromes in base 10\
 and base 2 is", get_pals(1e6))

