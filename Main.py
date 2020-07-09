import LastFm
import Timestamp

recentlyPlayedList = LastFm.lastDayTracks()
recentlyPlayedCount = 0
for item in recentlyPlayedList:
    recentlyPlayedCount += 1

print "-----  Recently Played  -----"
print "     Total Playbacks: " + str(recentlyPlayedCount)
for item in recentlyPlayedList:
    print str(item.playback_date) + "     " + str(item.track.artist) + " - " + str(item.track.title)


