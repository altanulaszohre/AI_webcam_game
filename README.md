# 🎮 AI Webcam Game

An interactive webcam-based game using **Mediapipe** and **Pygame** libraries.

---

## 🧠 About the Project

This is an AI-powered webcam game where the player controls game elements using hand gestures detected via their webcam. The game leverages **Mediapipe** for hand tracking and **Pygame** for visual game rendering.

https://user-images.githubusercontent.com/111522957/197341308-a489c9bf-e946-48e4-af5c-e61dfd670c28.mp4

---

## ⚙️ Technologies Used

- **Python**
- **Mediapipe** – for real-time hand gesture tracking via webcam
- **Pygame** – for rendering game components and UI
- **OpenCV** – optional (for additional camera controls or debugging)

---

## 🚀 How to Run

1. **Install dependencies**:
   ```bash
   pip install pygame mediapipe opencv-python
   ```

2. **Navigate to the project folder**:
   ```bash
   cd AI_webcam_game-main/code
   ```

3. **Run the game**:
   ```bash
   python main.py
   ```

Make sure your webcam is active and accessible when running the game.

---

## 🕹️ Controls

- Use **hand gestures** (open palm, closed fist, etc.) to interact with game elements.
- The AI detects your hand position and uses it as an input to control the plane or objects on the screen.

---

## 📁 Project Structure

```
AI_webcam_game-main/
│
├── code/
│   ├── main.py           # Main game loop
│   ├── setting.py        # Game settings
│   └── sprites.py        # Game sprite logic
│
├── img/                  # Game graphics and backgrounds
│   ├── menu.png
│   ├── plane0.png
│   └── ...
├── font/                 # Fonts used in the game
│
└── README.md
```

---

## 📸 Media

A short gameplay demonstration:

🎥 [Video Preview](https://user-images.githubusercontent.com/111522957/197341308-a489c9bf-e946-48e4-af5c-e61dfd670c28.mp4)

---

## 📄 License

This project is open source and available under the MIT License.

---

## 🙌 Acknowledgments

Special thanks to the creators of:
- [Mediapipe](https://github.com/google/mediapipe)
- [Pygame](https://www.pygame.org/)


***Altan Ulaş Zöhre***
