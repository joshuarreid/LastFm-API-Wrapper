from Token import lastfm_network, lastfm_username
import Timestamp



def getTracks(time_from, time_to):
    tracks = lastfm_network.get_user(lastfm_username).get_recent_tracks(cacheable=False, limit=None,
                                                                              time_from=time_from, time_to=time_to)
    return tracks


### impliment twentyFourHours Function to fetch the tracks from the last 24 Hours ###
def lastDayTracks():
    fromTime = fetchEST(currentYear, currentMonth, previousDay, currentHour, currentMinute)
    toTime = fetchEST(currentYear, currentMonth, currentDay, currentHour, currentMinute)
    lastDayTracks = getTracks(fromTime,toTime)
    return lastDayTracks








