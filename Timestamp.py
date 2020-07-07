from datetime import datetime
from time import mktime

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

timeStamps = {
    "time_from": 0,
    "time_to": 0,
}

currentMinute = datetime.now().minute
currentHour = datetime.now().hour
currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year
previousMonth = 0


def previousDay(day, month):
    if (day - 1) == 0:
        month -= 1
        previousDay = daysInMonth[month]
        return previousDay
    else:
        previousDay = (day-1)
        return previousDay


def fetchTimestamp(year, month, day, hour,minute):
    dt = datetime(year, month, day, hour-4, minute)
    est = mktime(dt.timetuple())
    return est

### FIX TO CHECK IF THE MONTH CHANGED ###
def twentyFourHours():
    yesterday = previousDay(currentDay, currentMonth)
    timeStamps["time_from"] = int(fetchTimestamp(currentYear, currentMonth, yesterday, currentHour, currentMinute))
    timeStamps["time_to"] = int(fetchTimestamp(currentYear, currentMonth, currentMinute, currentHour, currentMinute))







