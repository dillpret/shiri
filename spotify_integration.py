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
    sp.playlist_add_items(playlist_url, [track_link], position=0)


def get_song_search_term(track_link):
    track_details = sp.track(track_link)
    song_name = track_details['name']
    artist_name = track_details['artists'][0]['name']
    search_term = f'{song_name} {artist_name}'
    return search_term


def search_for_track_url(search_term):
    result = sp.search(search_term, limit=1, type='track')
    track_url = result['tracks']['items'][0]['external_urls']['spotify']
    return track_url
