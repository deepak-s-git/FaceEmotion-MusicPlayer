# spotify_player.py
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

class SpotifyPlayer:
    def __init__(self):
        self.client_id = os.getenv('SPOTIFY_CLIENT_ID')
        self.client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
        self.redirect_uri = os.getenv('SPOTIFY_REDIRECT_URI')
        self.scope = "user-read-playback-state,user-modify-playback-state"

        self.auth_manager = SpotifyOAuth(
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri=self.redirect_uri,
            scope=self.scope
        )
        self.sp = spotipy.Spotify(auth_manager=self.auth_manager)

        self.emotion_playlists = {
            'happy': 'spotify:playlist:37i9dQZF1DX3rxVfibe1L0',
            'sad': 'spotify:playlist:37i9dQZF1DX7qK8ma5wgG1',
            'angry': 'spotify:playlist:37i9dQZF1DX4eRPd9frC1m',
            'neutral': 'spotify:playlist:37i9dQZF1DX4sWSpwq3LiO',
            'surprised': 'spotify:playlist:37i9dQZF1DX0BcQWzuB7ZO',
            'fear': 'spotify:playlist:37i9dQZF1DX6SpcerLm4x7',
            'disgust': 'spotify:playlist:37i9dQZF1DWUk47CLxI4Uo'
        }

    def play_playlist_for_emotion(self, emotion):
        uri = self.emotion_playlists.get(emotion, self.emotion_playlists['neutral'])
        try:
            devices = self.sp.devices()
            if not devices['devices']:
                print("No active Spotify device found.")
                return False

            self.sp.start_playback(context_uri=uri)
            print(f"Now playing {emotion} playlist")
            return True
        except Exception as e:
            print(f"Error playing {emotion} playlist: {e}")
            return False
