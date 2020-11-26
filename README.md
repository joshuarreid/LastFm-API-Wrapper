# Statify

## Description
This project builds upon the API Wrapper [Pylast](https://github.com/pylast/pylast) providing more functionality and features catered towards my own needs.

## Functionality

### playbackTimeUtcToEst(utcTime) 
* utcTime - unix timestamp in UTC time
returns the converted playback time from UTC time zone to EST time zone

### getTracksTimeInterval(timeFrom, timeTo, user)
* timeFrom - unix timestamp starting time
* timeTo - unix timestamp end time
* user - Last.Fm username
returns a users played tracks within a time interval

### playbackPastDay(user)
* user - Last.Fm username
returns a list of users played tracks from last 24 hours

### playbackPastThreeHours(user)
* user - Last.Fm username
returns a list of users played tracks from past 3 hours

### oneYearAgoTracks(user)
* user - Last.Fm username
returns a list of users played tracks from within the same hour one year ago

### getNowPlaying(user)
* user - Last.Fm username
returns a users currently playing track

### getTopTracks(user, periodInput)
* user - Last.Fm username
* periodInput - (*String*) "overall", "7day", "1month", "3month", "6month", or "12month"
returns a list of users top tracks within the periodInput

### getTopArtist(user, periodInput)
* user - Last.Fm username
* periodInput - (*String*) "overall", "7day", "1month", "3month", "6month", or "12month"
returns a list of users top artists within the periodInput

### playCount(user)
* user - Last.Fm username
returns a users total playback count

### compareUsersTopTracks(user, otherUser, periodInput)
* user - Last.Fm username
* otherUser - another Last.Fm username
* periodInput - (*String*) "overall", "7day", "1month", "3month", "6month", or "12month"
returns a list of the intersections between two users' top tracks

### compareUsersTopArtists(user, otherUser, periodInput)
* user - Last.Fm username
* otherUser - another Last.Fm username
* periodInput - (*String*) "overall", "7day", "1month", "3month", "6month", or "12month"
returns a list of the intersections between two users' top artists






