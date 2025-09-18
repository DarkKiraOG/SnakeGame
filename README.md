SnakeGame
---------

A Python implementation of the classic Snake game. Control the snake, eat food, avoid collision, and try to get the highest score possible.

---------

Features
---------
- Playable Snake game with increasing score
- Food appears at random positions
- Collision detection with walls and the snake’s own body
- Keeps scoreboard of highest scores

---------

Requirements
---------
- Python 3.6 or later
- Libraries: turtle, time, random
- Works on Windows, macOS, and Linux

---------

Installation
---------
1. Clone this repository:
   git clone https://github.com/DarkKiraOG/SnakeGame.git
   cd SnakeGame

2. Install dependencies (if any):
   pip install -r requirements.txt

---------

Usage
---------
Run the game with:
   python main.py

Controls:
- Arrow keys to move the snake
  
Gameplay:
- Each time you eat food, your score increases and the snake gets longer
- The game ends if the snake collides with the wall or itself
- The score is shown continuously at the top of the screen
- High scores are saved (to Data.txt)

---------

Project Structure
---------
SnakeGame/
├── main.py            (Entry point for the game)
├── snake.py           (Snake logic: movement, growth, collision)
├── food.py            (Food spawning logic)
├── scoreboard.py      (Tracking and storing high scores)
├── Data.txt           (File to store high scores)
├── __pycache__/       (Compiled Python files)
└── README.txt         (Project documentation)

---------

How to Contribute
---------
1. Create an issue describing a bug or feature request
2. Fork the project
3. Create a new branch (git checkout -b feature-name)
4. Make your changes
5. Submit a pull request

---------

License
---------
This project is licensed under the MIT License. You are free to use, modify, and share it.

---------

Tags
---------
python, game, snake, arcade, console, classic
