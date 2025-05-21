# main.py
import cv2
import numpy as np
import time
from deepface import DeepFace
from spotify_player import SpotifyPlayer

class EmotionMusicPlayer:
    def __init__(self):
        self.spotify = SpotifyPlayer()
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        self.current_emotion = None
        self.emotion_count = {emo: 0 for emo in self.spotify.emotion_playlists}
        self.emotion_threshold = 3
        self.last_emotion_time = time.time()
        self.cooldown = 15  # seconds
        self.frame_skip = 5
        self.frame_counter = 0

    def detect_emotion(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

        if len(faces) > 0:
            largest_face = max(faces, key=lambda rect: rect[2] * rect[3])
            x, y, w, h = largest_face
            roi = frame[y:y+h, x:x+w]

            try:
                result = DeepFace.analyze(roi, actions=['emotion'], enforce_detection=False)
                emotion = result[0]['dominant_emotion'].lower()
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(frame, f"Emotion: {emotion}", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
                return emotion
            except Exception as e:
                print("DeepFace Error:", e)
                return None
        return None

    def run(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Webcam not accessible.")
            return

        print("Press 'q' to quit.")
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            self.frame_counter += 1
            if self.frame_counter % self.frame_skip == 0:
                emotion = self.detect_emotion(frame)
                if emotion:
                    self.emotion_count[emotion] += 1
                    for e in self.emotion_count:
                        if e != emotion:
                            self.emotion_count[e] = 0

                    if (self.emotion_count[emotion] >= self.emotion_threshold and
                        (self.current_emotion != emotion or
                         time.time() - self.last_emotion_time > self.cooldown)):
                        print(f"Detected consistent emotion: {emotion}")
                        if self.spotify.play_playlist_for_emotion(emotion):
                            self.current_emotion = emotion
                            self.last_emotion_time = time.time()

            cv2.imshow('Emotion Detector', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    EmotionMusicPlayer().run()
