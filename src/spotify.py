import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import dotenv_values

CONFIG = dotenv_values(".env")


class SpotifyContext:
    """
    Singleton class for communicating with the Spotify API
    """
    _instance = None
    _context = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__connect()
        return cls._instance

    def __connect(self):
        self._context = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=CONFIG["CLIENT_ID"],
            client_secret=CONFIG["CLIENT_SECRET"],
            redirect_uri='http://127.0.0.1:8888/callback',
            scope='user-read-playback-state user-modify-playback-state playlist-read-private'
        ))

    def test(self):
        current = self._context.current_playback()
        print(current)

