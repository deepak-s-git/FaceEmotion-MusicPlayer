# 🎵 Face Emotion-Based Music Recommender

Detects your facial emotion in real-time using DeepFace and plays a matching Spotify playlist.

## ✅ Features

- Real-time face emotion detection via webcam
- Spotify playback based on emotion
- Smooth frame processing & emotion debouncing

## 🔧 Setup

1. **Clone the repository**  

2. **Install dependencies**  

3. **Set up your `.env` file**  
Create a `.env` file with:
SPOTIFY_CLIENT_ID=your_id
SPOTIFY_CLIENT_SECRET=your_secret
SPOTIFY_REDIRECT_URI=http://127.0.0.1:8888/callback


4. **Run the project**  

## 🧠 Emotion → Playlist Mapping

| Emotion    | Spotify Playlist |
|------------|------------------|
| happy      | Mood Booster     |
| sad        | Life Sucks       |
| angry      | Rock Hard        |
| neutral    | Chill Vibes      |
| surprised  | Fresh Finds      |
| fear       | Dark & Stormy    |
| disgust    | Anti Pop         |

## 📷 Notes

- Ensure your face is clearly visible in good lighting.
- Make sure a Spotify device (phone, PC, etc.) is **active and open**.

---

## 💡 Improvements

- Smoothened frame processing using frame skipping.
- Emotion debounce logic to prevent multiple triggers for same emotion.
