import pylast
from Token import lastfm_username, lastfm_network
from datetime import datetime
from time import mktime



### Testing Getting Recent Tracks ###
recentTracks = lastfm_network.get_user(lastfm_username).get_recent_tracks(cacheable=False, limit=None, time_from=1593907200,time_to=1593993600)
for item in recentTracks:
    print str(item.playback_date) + "     " + str(item.track.artist) + " - " + str(item.track.title)



### Testing getting current times ###
currentMinute = datetime.now().minute
currentHour = datetime.now().hour
currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year
print "the current month is: " + str(currentMonth)



### Testing unix timestamp conversion of current time ###
dt = datetime(currentYear, currentMonth, currentDay, currentHour, currentMinute)
unx = mktime(dt.timetuple())
print "The UTC unix timestamp for right now is: " + str(unx)


### unix timestamp function ###
def unixTime(year, month, day, hour, minute):
    dt = datetime(year, month, day, hour, minute)
    unx = mktime(dt.timetuple())
    return unx


### Testing UTC to EST Converter Function ###
def fetchEST(year, month, day, hour,minute):
    dt = datetime(year, month, day, hour-4, minute)
    EST = int(mktime(dt.timetuple()))
    return EST
print "The Function fetchEST outputted: " + str(fetchEST(currentYear, currentMonth, currentDay, currentHour,currentMinute))



### Function finds what the date was for previous day and checks if its the beginning of a month ###
def previousDate(day, month, year):
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
    yesterday = {
        "month": month,
        "day": day,
        "year" : year
    }
    if (day - 1) == 0: # if that date is the first
        if month == 1: # if the month is january
            yesterday["month"] = 12
            yesterday["year"] -= 1
            yesterday["day"] = daysInMonth[12]
            return yesterday
        else: # if the month is not january
            yesterday["month"] -= 1
            yesterday["day"] = daysInMonth[yesterday["month"]]
            month -= 1
            return yesterday

    else:
        yesterday["day"] -= 1
        return yesterday




# Testing get timestamps for last 24 Hours ###
from Timestamp import timeStamps
from Timestamp import fetchTimestamp


def twentyFourHours():
    yesterday = previousDate(currentDay, currentMonth, currentYear)
    timeStamps["time_from"] = fetchTimestamp(yesterday["year"], yesterday["month"], yesterday["day"], currentHour, currentMinute)
    timeStamps["time_to"] = fetchTimestamp(currentYear, currentMonth, currentDay, currentHour, currentMinute)
    return timeStamps


twentyFourHours()
print " "
print "twentyFourHours() Outputted: " + "Time_from = " + str(timeStamps["time_from"])
print "twentyFourHours() Outputted: " + "Time_to = " + str(timeStamps["time_to"])












### Testing Getting Recent Tracks ###
recentTracks = lastfm_network.get_user(lastfm_username).get_recent_tracks(cacheable=False, limit=None, time_from=1593907200,time_to=1593993600)
print " "
print "Tracks from July 5th 2020: "
for item in recentTracks:
    print str(item.playback_date) + "     " + str(item.track.artist) + " - " + str(item.track.title)



### Testing Getting Tracks Function ###
def getTracks(time_from, time_to):
    tracks = lastfm_network.get_user(lastfm_username).get_recent_tracks(cacheable=False, limit=None,
                                                                              time_from=time_from, time_to=time_to)
    return tracks
print " "
print "getTracks(July 5th 2020) Outputted: "
getTracksTest = getTracks(1593907200, 1593993600)
for item in getTracksTest:
    print str(item.playback_date) + "     " + str(item.track.artist) + " - " + str(item.track.title)



### Testing Getting Tracks from last 24 Hours ###
previousDayValue = int(currentDay) - 1
fromTime = fetchEST(currentYear, currentMonth, previousDayValue, currentHour, currentMinute)
toTime = fetchEST(currentYear, currentMonth, currentDay, currentHour, currentMinute)
lastDayTracks = lastfm_network.get_user(lastfm_username).get_recent_tracks(cacheable=True, limit=None, time_from=int(fromTime),time_to=int(toTime))
print " "
print "Tracks from Last 24 Hours: "
for item in lastDayTracks:
    print str(item.playback_date) + "     " + str(item.track.artist) + " - " + str(item.track.title)



### Testing Getting Tracks from last 24 hours Function ###
def lastDayTracks():
    currentMinute = datetime.now().minute
    currentHour = datetime.now().hour
    currentDay = datetime.now().day
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    previousDayValue = int(currentDay) - 1

    fromTime = fetchEST(currentYear, currentMonth, previousDayValue, currentHour, currentMinute)
    toTime = fetchEST(currentYear, currentMonth, currentDay, currentHour, currentMinute)
    lastDayTracks = getTracks(fromTime,toTime)
    return lastDayTracks

lastDayTracksFunction = lastDayTracks()
print " "
print "lastDayTracks() Outputted: "
for item in lastDayTracksFunction:
    print str(item.playback_date) + "     " + str(item.track.artist) + " - " + str(item.track.title)


### Testing Get Tracks from this time last year ###
def yearAgoTracks():
    currentMinute = datetime.now().minute
    currentHour = datetime.now().hour
    currentDay = datetime.now().day
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    previousYear = int(currentYear) - 1
    previousHour = int (currentHour) - 1

    fromTime = fetchEST(previousYear, currentMonth, currentDay, previousHour, currentMinute)
    toTime = fetchEST(previousYear, currentMonth, currentDay, currentHour, currentMinute)
    yearAgoTracks = getTracks(fromTime,toTime)
    return yearAgoTracks

yearAgoTracksFunction = yearAgoTracks()
print " "
print "yearAgoTracks() Outputted: "
for item in yearAgoTracksFunction:
    print str(item.playback_date) + "     " + str(item.track.artist) + " - " + str(item.track.title)



### Testing function grabbing tracks from last 24 hours ###
def lastDayTracks():
    lastDayTracksList = getTracks(int(timeStamps["time_from"]),int(timeStamps["time_to"]))
    return lastDayTracksList


lastDayTracksList = lastDayTracks()
print " "
print "lastDayTracks() Outputted: "
for item in lastDayTracksList:
    print str(item.playback_date) + "     " + str(item.track.artist) + " - " + str(item.track.title)

