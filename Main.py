import pylast
from Token import lastfm_network
import LastFm
import Timestamp

lastDayTracksList = LastFm.lastDayTracks()
print "Last 24 Hours: "
for item in lastDayTracksList:
        print str(item.playback_date) + "     " + str(item.track.artist) + " - " + str(item.track.title)


