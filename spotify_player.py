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

        self.emotion_tracks = {
            'happy': [
                'spotify:track:0HcHPBu9aaF1MxOiZmUQTl',  # Pharrell Williams - Happy
                'spotify:track:1rfofaqEpACxVEHIZBJe6W'   # Justin Timberlake - CAN'T STOP THE FEELING!
            ],
            'sad': [
                'spotify:track:4ZxkOaZ9j7TzjYQeC6zU8x',  # Lewis Capaldi - Someone You Loved
                'spotify:track:1rqqCSm0Qe4I9rUvWncaom'   # Adele - Easy On Me
            ],
            'angry': [
                'spotify:track:1lCRw5FEZ1gPDNPzy1K4zW',  # Linkin Park - One Step Closer
                'spotify:track:0O45fw2L5vsWpdsOdXwNAR'   # Rage Against The Machine - Killing In the Name
            ],
            'neutral': [
                'spotify:track:3AJwUDP919kvQ9QcozQPxg',  # Queen – Don’t Stop Me Now
                'spotify:track:2takcwOaAZWiXQijPHIx7B'   # The Chainsmokers - Closer
            ],
            'surprised': [
                'spotify:track:3Zwu2K0Qa5sT6teCCHPShP',  # Imagine Dragons - Thunder
                'spotify:track:0VjIjW4GlUZAMYd2vXMi3b'   # The Weeknd - Blinding Lights
            ],
            'fear': [
                'spotify:track:6RRNNciQGZEXnqk8SQ9yv5',  # Billie Eilish - Bury A Friend
                'spotify:track:7BqBn9nzAq8spo5e7cZ0dJ'   # Eminem - Lose Yourself
            ]
        }

    def play_tracks_for_emotion(self, emotion):
        track_uris = self.emotion_tracks.get(emotion, self.emotion_tracks['neutral'])
        try:
            devices = self.sp.devices()
            if not devices['devices']:
                print("No active Spotify device found.")
                return False

            self.sp.start_playback(uris=track_uris)
            print(f"Now playing tracks for emotion: {emotion}")
            return True
        except Exception as e:
            print(f"Error playing tracks for emotion '{emotion}': {e}")
            return False