# import the built-in library datetime
import datetime
# get today's date as a date object
today = datetime.date.today()
# add 1 week to today's date
newdate = today + datetime.timedelta(weeks=1)
# convert date object to string
today_str = today.strftime('%d-%m-%Y')
newdate_str = newdate.strftime('%d-%m-%Y')

print(today)
print(newdate)
