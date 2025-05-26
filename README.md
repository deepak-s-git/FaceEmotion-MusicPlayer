# 🎵 Face Emotion-Based Music Player

Detect your real-time facial emotion and play matching Spotify tracks automatically.

## ✅ Features

* Real-time face emotion detection via webcam (DeepFace)
* Spotify playback of curated tracks based on detected emotion
* Emotion debounce and cooldown logic to avoid rapid switches
* Configurable detection threshold and cooldown duration

## 🔧 Setup

1. **Clone the repository**

   ```bash
   git clone <repo_url>
   cd <repo_name>
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   Create a `.env` file in the project root with:

   ```env
   SPOTIFY_CLIENT_ID=your_spotify_client_id
   SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
   SPOTIFY_REDIRECT_URI=http://localhost:8888/callback
   ```

4. **Adjust detection settings (optional)**
   In `main.py`:

   * `emotion_threshold`: Number of consistent detections before switching (default: 5)
   * `cooldown`: Minimum seconds to wait before allowing a new emotion (default: 60)

5. **Run the application**

   ```bash
   python main.py
   ```

## 🎯 Emotion → Track Mapping

| Emotion  | Track Examples                                   |
| -------- | ------------------------------------------------ |
| happy    | Pharrell Williams – "Happy"                      |
|          | Justin Timberlake – "Can’t Stop The Feeling"     |
| sad      | Lewis Capaldi – "Someone You Loved"              |
|          | Adele – "Easy On Me"                             |
| angry    | Linkin Park – "One Step Closer"                  |
|          | Rage Against The Machine – "Killing in the Name" |
| neutral  | Queen – "Don’t Stop Me Now"                      |
|          | The Chainsmokers – "Closer"                      |
| surprise | Imagine Dragons – "Thunder"                      |
|          | The Weeknd – "Blinding Lights"                   |
| fear     | Billie Eilish – "Bury a Friend"                  |
|          | Eminem – "Lose Yourself"                         |

> **Note:** The `disgust` emotion mapping has been removed.

## 📷 Usage Notes

* Ensure your face is well-lit and within the webcam frame.
* Have an active Spotify device open (desktop or mobile) under the same account.
* The app requires authorization on first run; follow the provided URL.

---

## 💡 Improvements

* Frame skipping for performance and smoother detection.
* Debouncing logic ensures tracks play long enough before switching.
* Easily extendable mapping in `spotify_player.py` for more emotions or tracks.

