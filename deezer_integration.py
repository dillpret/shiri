import requests

DEEZER_SEARCH_URL = "https://api.deezer.com/search";


def add_to_deezer_playlist(token, song_details, playlist_url):
    search_params = {'access_token': token, 'q': song_details}
    search_response = requests.get(DEEZER_SEARCH_URL, params=search_params).json()
    song_id = search_response['data'][0]['id']
    song_link = search_response['data'][0]['link']

    add_params = {'access_token': token, 'songs': song_id, 'request_method': 'POST'}
    requests.get(playlist_url, params=add_params)
    return song_link
