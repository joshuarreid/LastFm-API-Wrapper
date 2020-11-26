# Statify

## Description
This project builds upon the API Wrapper [Pylast](https://github.com/pylast/pylast) providing more functionality and features catered towards my own needs.

## Functionality
<br />
### playbackTimeUtcToEst(utcTime) 
* utcTime - unix timestamp in UTC time
converts playback time from UTC time zone to EST time zone

### getTracksTimeInterval(timeFrom, timeTo, user)
* timeFrom - unix timestamp starting time
* timeTo - unix timestamp end time
* user - Last.Fm username
grabs a users played tracks within a time interval

