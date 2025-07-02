## Snake Game 🐍

A classic Snake game built in Python using the `turtle` graphics module.

```

day-20/
├── food.py
├── main.py        # entry point; run this to start the game
├── snake.py
├── scoreboard.py
├── requirements.txt
└── README.md

````

## Getting Started

### Prerequisites

- Python 3.7 or higher  
- (Optional) virtual environment tool: `python -m venv .venv`

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/<YOUR-USERNAME>/day-20-snake.git
cd day-20-snake

# 2. (Optional) Create & activate a virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
````

## How to Play

```bash
python main.py
```

* Use the **arrow keys** to move the snake.
* Eat the food to grow longer.
* Don’t run into the walls or the snake’s own tail!

## Features

* **Modular code**: `snake.py`, `food.py`, and `scoreboard.py` each handle their own logic.
* **Score tracking**: The scoreboard increases as you eat food and resets on collision.
* **Clean exit**: Click the window’s close button to end the game.

## Dependencies

Listed in `requirements.txt`:

```
turtle
```

## License

This project is licensed under the [MIT License](LICENSE).

