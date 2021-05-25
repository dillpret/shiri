import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()
SPOTIFY_ACCESS_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_SEARCH_URL = "https://api.spotify.com/v1/search"

scope = "playlist-modify-public"
auth_manager = SpotifyOAuth(scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)


def is_spotify_link(string):
    regex = r'^(spotify:|https://[a-z]+\.spotify\.com/)'
    if re.search(regex, string):
        return True
    else:
        return False


def add_to_spotify_playlist(track_link, playlist_url):
    sp.playlist_add_items(playlist_url, [track_link])


# search_results = sp.search(args, type='track')
    # print(search_results)
