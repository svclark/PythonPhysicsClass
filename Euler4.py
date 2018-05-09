#Project Euler Problem 4

def ispalindrome(string):
  length = len(string)
  pal = False
  for i in range(0, length):
    if (string[length-1-i] == string[i]):
      if(i == 5):
        return True
        break
    else:
      return False

  return pal

def palindrome():
  numbers = []
  pal = "poop"
  for i in range(100, 1000):
    numbers.append(i)

  roducts = []
  for i in range(0, len(numbers)):
    for j in range(0, len(numbers)):
      roducts.append(numbers[i]*numbers[j])

  products = roducts[::-1]

  allpal = []
  for i in range(0,len(products)):
    if(ispalindrome(str(products[i]))):
      allpal.append(products[i])

  return max(allpal)


print(palindrome())
