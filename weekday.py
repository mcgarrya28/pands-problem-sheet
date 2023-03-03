# Python Weekday
# Author: Anthony Mc Garry

import datetime

today = datetime.datetime.today().weekday()

# Where the day is less 5 weekday

if today < 5:
    print("Today is a weekday.")
else:
    print("Today is a weekend day.")