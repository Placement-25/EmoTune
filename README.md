# 🎧 EmoTune – Emotion-Aware Lifestyle Companion

**EmoTune** is a real-time facial emotion recognition system that dynamically adapts the user experience including music, UI themes, and feedback based on your current mood. Powered by **React**, **Flask**, **MongoDB**, and **DeepFace**, this project blends computer vision, user experience design, and emotional intelligence into a unified lifestyle assistant.

---

## 🚀 Tech Stack

- **Frontend**: React (interactive UI, theme switching, camera/file upload)
- **Backend**: Flask (REST API for emotion detection)
- **Computer Vision**: DeepFace + OpenCV (real-time emotion analysis)
- **Database**: MongoDB (emotion history & logs)
- **Integration Ready**: Spotify API, YouTube Data API (mood-based music)

---

## 🧠 Key Features

### 🎥 Emotion Detection
- Real-time facial emotion recognition using webcam or uploaded images
- Powered by DeepFace with facial expression analysis (happy, sad, angry, etc.)

### 🎵 Mood-Based Music Control *(Pluggable)*
- Dynamically trigger music playlists based on detected emotion
- Optional Spotify or YouTube integration for seamless streaming

### 🎨 Adaptive UI Theme
- Frontend dynamically changes color themes to match mood:
  - 🟢 Happy → Bright Theme  
  - 🔵 Sad → Cool Blue  
  - 🔴 Angry → Dark Mode  

### 📊 Emotion Tracking
- Logs all detected emotions with timestamps in MongoDB
- Easily expandable to visualize emotion trends over time

### 🧩 Modular Architecture
- Flask API modularized for CV, logging, and third-party integrations
- Easily deployable and scalable microservice structure

---

## 📂 Project Structure

```

emotune/
├── backend/            # Flask backend with DeepFace + MongoDB
├── frontend/           # React frontend with webcam/file input
└── README.md           # Project documentation

```

---

## 📌 Roadmap Ideas

- [ ] Real-time webcam streaming with continuous emotion polling
- [ ] Emotion trend graphs (weekly/monthly)
- [ ] Personalized user profiles and emotion history
- [ ] Spotify/YouTube playlist recommendation engine
- [ ] Mobile PWA or native version

---

## 🤝 Contributing

Contributions are welcome! Please fork the repo and submit a pull request with your improvements or ideas.

---


