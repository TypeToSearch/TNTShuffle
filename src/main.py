import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Replace these with your app credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    redirect_uri='http://localhost:8888/callback',
    scope='user-read-playback-state user-modify-playback-state playlist-read-private'
))
