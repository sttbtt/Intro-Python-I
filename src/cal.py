"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should 
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that 
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

calendar.setfirstweekday(calendar.SUNDAY)
now = datetime.now()

while True:
  m = sys.argv[1]
  # m = input('Enter month: ') or now.month
  
  try:
    month = int(m)
  except ValueError:
    print("This is not a valid month, please use numbers 1 - 12 in the form of MM")
    exit()
  else:
    break

while True:
  y = sys.argv[2]
  # y = input('Enter year: ') or now.year

  try:
    year = int(y)
  except ValueError:
    print("This is not a valid year, please use numbers in the form of YYYY")
    exit()
  else:
    break

print()
print(calendar.month(year, month))
