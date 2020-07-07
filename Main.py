import pylast
from Token import API_KEY, API_SECRET, lastfm_username, lastfm_password_hash
from LastFm import getPastDay



lastfm_network = pylast.LastFMNetwork(
    api_key = API_KEY,
    api_secret=API_SECRET,
    username=lastfm_username,
    password_hash=lastfm_password_hash,
)

getPastDay()





