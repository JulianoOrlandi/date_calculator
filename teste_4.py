import time
import datetime

year = 1582
leap_years = []

for i in range(0, (1983 - 1582)):
    if (year % 4) == 0:
         if (year % 100) != 0:
              leap_years.append(year)
         elif (year % 400) == 0:
              leap_years.append(year)
    year += 1

print(leap_years)
print(len(leap_years))