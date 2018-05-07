import numpy as np

months = {'Jan':31, "Feb":28, "Mar":31, "Apr":30, "May":31, "Jun":30,"Jul":31, "Aug":31, "Sep":30, "Oct":31, "Nov":30,"Dec":31}

dm = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dow = [1,2,3,4,5,6,7]

sundays = 0
thisday = 2 #Jan 1, 1901 was a Tuesday (2sday)
for yy in range(1901, 2000+1):
  print("\n\n",yy)
  for mm in range(0,len(dm)):
    if(yy % 4 == 0 ):
      dm[1] = 29
    else: dm[1] = 28
    print(dm[mm])
    for dd in range(0, dm[mm]):

        thisday += 1
        if(thisday == 8): thisday = 1
        print(thisday)

        if(thisday == 7 and dd == 0):
          sundays += 1
  dm[1] = 28

print(sundays)


