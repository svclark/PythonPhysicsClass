nums = ["one","two","three","four","five","six","seven","eight","nine"]
nums2 = ["","one","two","three","four","five","six","seven","eight","nine"]

teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

hun = "hundred"
an = "and"

thisstring = ""
#Count 1-9
for i in range(0, len(nums)):
  thisstring += nums[i]

#Count 10-19
for i in range(0, len(teens)):
  thisstring += teens[i]

#Count 20-99
for i in range(0, len(tens)):
  for j in range(0, len(nums2)):
    thisstring += tens[i] + nums2[j]

#Count *00-*09
for i in range(0, len(nums)):
  for j in range(0, len(nums2)):
    if(j == 0):
      thisstring += nums[i] + hun
    else:
      thisstring += nums[i] + hun + an + nums2[j]

#Count *10-*19
for i in range(0, len(nums)):
  for j in range(0, len(teens)):
    thisstring += nums[i] + hun + an + teens[j]

#Count *20-*99
for i in range(0, len(nums)):
  for j in range(0, len(tens)):
    for k in range(0, len(nums2)):
      thisstring += nums[i] + hun + an + tens[j] + nums2[k]

thisstring += "onethousand"

#print(thisstring)
print(len(thisstring))
