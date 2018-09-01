# coding: utf-8

import spotipy
import spotipy.util as util

CLIENT_ID = '0653e348f6134e17afe2533c3307bb48'
CLIENT_SECRET = '147ceb6e7e3b4139aac65bfdebbf9557'
USER = '12180777012'
DISPLAY = 'Max Pham'
scope = 'user-read-playback-state' #https://developer.spotify.com/web-api/using-scopes/

def current_user_playing_track(spot):
        ''' Get information about the current users currently playing track.
        '''
        return spot._get('me/player/currently-playing')

def current_user_playing(spot):
        ''' Get information about the current users currently playing.
        '''
        return spot._get('me/player')


###### AUTH
token = util.prompt_for_user_token(USER, scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri='http://localhost/')
spotify = spotipy.Spotify(auth=token)

###### COLLECTION

### Currently playing title

def get_data():
    data, current_player  = current_user_playing_track(spotify), current_user_playing(spotify)

    current_device = current_player['device']['name']
    current_title = data["item"]['name']
    current_artist = data["item"]["artists"][0]["name"]

    return current_title, current_artist, current_device
