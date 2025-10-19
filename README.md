# 🏓 Pygame Ping Pong Game

A simple real-time **Ping Pong game** built using **Python and Pygame**, featuring:
- Realistic paddle and ball movement
- AI opponent
- Score tracking
- Game-over screen with replay options (Best of 3, 5, or 7)
- Sound effects for hits, bounces, and scoring

---

## 🎮 Gameplay

- **Controls**:  
  - `W` – Move player paddle up  
  - `S` – Move player paddle down  
  - `3`, `5`, `7` – Select Best-of mode after a game ends  
  - `ESC` – Exit the game

- **Objective**:  
  First to reach the set number of points wins! After a game, you can replay without restarting the program.

---

## 🔊 Sound Effects

Place your `.wav` sound files in an `assets/` folder at the project root:

---

## 🛠️ Installation and Setup

Follow these steps to install and run the Ping Pong game on your system:

### 1. Clone or Download the Repository
If you’re using Git:
```bash
git clone https://github.com/niranjinii/ping-pong.git
cd ping-pong
````

Or simply download the ZIP file from your repository and extract it.

---

### 2. Set Up a Virtual Environment (Optional but Recommended)

Create and activate a virtual environment to keep dependencies isolated.

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

Use the provided `requirements.txt` file to install all necessary packages:

```bash
pip install -r requirements.txt
```

---

### 4. Add Sound Assets

Make sure your project has an `assets/` folder containing the following `.wav` files:

```
assets/
├── paddle_hit.wav
├── wall_bounce.wav
└── score.wav
```

You can download them from these free sources:

* [Paddle Hit](https://freesound.org/people/Monster_1999_Kyle/sounds/653392/)
* [Wall Bounce](https://pixabay.com/sound-effects/bouncing-ball-sound-effect-by-engyclick-280716/)
* [Score Sound](https://pixabay.com/sound-effects/achievement-bell-6007/)

---

### 5. Run the Game

Once everything is set up, launch the game with:

```bash
python main.py
```

---

### 6. Controls

| Key           | Action                                |
| ------------- | ------------------------------------- |
| **W**         | Move paddle up                        |
| **S**         | Move paddle down                      |
| **3 / 5 / 7** | Choose Best-of mode after a game ends |
| **ESC**       | Exit the game                         |

---

