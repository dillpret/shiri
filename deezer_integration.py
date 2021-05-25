import requests

DEEZER_SEARCH_URL = "https://api.deezer.com/search";

# The real one
# DEEZER_PLAYLIST_URL = "https://api.deezer.com/playlist/8866431842/tracks"

# Test
DEEZER_PLAYLIST_URL = "https://api.deezer.com/playlist/9104256582/tracks"


def add_to_deezer_playlist(token, song_details):
    search_params = {'access_token': token, 'q': song_details}
    search_response = requests.get(DEEZER_SEARCH_URL, params=search_params).json()
    song_id = search_response['data'][0]['id']
    song_link = search_response['data'][0]['link']

    add_params = {'access_token': token, 'songs': song_id, 'request_method': 'POST'}
    requests.get(DEEZER_PLAYLIST_URL, params=add_params)
    return song_link
