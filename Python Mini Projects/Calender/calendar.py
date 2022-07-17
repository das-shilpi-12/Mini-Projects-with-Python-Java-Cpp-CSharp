#please enter a valid year and month details
#year details can be year 1 - till now
#month details should be 1-12

import calendar 
year = int(input("Enter the year: \n"))
month = int(input("Enter the month: \n"))
print(year,"\n")
print(month,"\n")
print (calendar.month(year,month))
