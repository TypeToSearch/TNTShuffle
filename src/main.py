import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import dotenv_values

CONFIG = dotenv_values(".env")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CONFIG["CLIENT_ID"],
    client_secret=CONFIG["CLIENT_SECRET"],
    redirect_uri='http://127.0.0.1:8888/callback',
    scope='user-read-playback-state user-modify-playback-state playlist-read-private'
))

current = sp.current_playback()
print(current)

