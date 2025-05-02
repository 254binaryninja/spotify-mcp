## Create the various spotify methods which will be used to interact with the Spotify API

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from settings import settings

## Create the Spotify client
try:
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=settings.SPOTIFY_CLIENT_ID,
        client_secret=settings.SPOTIFY_CLIENT_SECRET,
        redirect_uri="http://127.0.0.1:8888/callback",
        scope="user-read-playback-state user-modify-playback-state user-library-read user-library-modify playlist-modify-public playlist-modify-private"
    ))
except Exception as e:
    import sys
    print(f"Spotify authentication failed: {e}", file=sys.stderr)

