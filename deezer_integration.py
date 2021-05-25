import requests

DEEZER_SEARCH_URL = "https://api.deezer.com/search";
DEEZER_PLAYLIST_URL = "https://api.deezer.com/playlist/8866431842/tracks"


def add_to_deezer_playlist(token, song_details):
    search_params = {'access_token': token, 'q': song_details}
    search_response = requests.get(DEEZER_SEARCH_URL, params=search_params).json()
    song_id = search_response['data'][0]['id']

    add_params = {'access_token': token, 'songs': song_id, 'request_method': 'POST'}
    requests.get(DEEZER_PLAYLIST_URL, params=add_params)
    print(search_response)
