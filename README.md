# Number Guessing Game

A simple command-line game where the computer selects a random number between 1 and 100,
and you try to guess it. After each guess, the program tells you whether your guess
is too high or too low until you find the correct number.

## How to Run

1. **Clone the repository**

   ```bash
   git clone https://github.com/USERNAME/number-guessing-game.git
   cd number-guessing-game
2. **Create and activate a virtual environment**

python -m venv venv      # Windows
# or
python3 -m venv venv    # macOS / Linux

source venv/bin/activate  # macOS / Linux
.\venv\Scripts\activate    # Windows

3. **Run the game**

python guess.py          # Windows
# or
python3 guess.py         # macOS / Linux

## Features

Random number generation (1–100)
Input validation with error handling
Feedback on each guess (“Too high!” / “Too low!”)
Tracks the number of attempts
