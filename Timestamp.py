from datetime import datetime
from time import mktime

### Dictionary that keeps record of how many days in each month ###
daysInMonth = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,

}

### Dictionary that holds time variables for use in functions from LastFm.py ###
timeStamps = {
    "time_from": 0,
    "time_to": 0,
}

### Fetching current time and storing them in variables ###
currentMinute = datetime.now().minute
currentHour = datetime.now().hour
currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year
previousMonth = 0


### Function finds what the date was for previous day and checks if its the beginning of a month ###
def previousDay(day, month):
    if (day - 1) == 0:
        month -= 1
        previousDayValue = daysInMonth[month]
        return previousDayValue
    else:
        previousDayValue = (day - 1)
        return previousDayValue


### Create previousMonth Function ###


### fetches timestamp in EST for a given date ###
def fetchTimestamp(year, month, day, hour,minute):
    dt = datetime(year, month, day, hour-4, minute)
    est = mktime(dt.timetuple())
    return est


### Grabs timestamps from 24 hours ago to current time ###
### FIX TO CHECK IF THE MONTH CHANGED ###
def twentyFourHours():
    yesterday = previousDay(currentDay, currentMonth)
    timeStamps["time_from"] = fetchTimestamp(currentYear, currentMonth, yesterday, currentHour, currentMinute)
    timeStamps["time_to"] = fetchTimestamp(currentYear, currentMonth, currentDay, currentHour, currentMinute)
    return timeStamps










