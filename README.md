# Match & Catch

## 📌 Project Overview

Match & Catch is a console-based memory game built in Python. 
It displays a hidden grid of randomized integer pairs, which the player must uncover by guessing two cells at a time.
The game tracks performance using a scoring system based on the number of guesses made, and offers features such as grid reveals, restarts, and interactive feedback.
It emphasizes memory recall and input handling while reinforcing core Python concepts.

---

## 📁 Project Structure

- `game.py` Contains the user interface, menu system, command-line argument validation, user prompts, and game loop.
- `grid.py` Implements the Grid class, which manages the game board, value matching, revealing logic, and score calculation.

---

## 🔧 Features (Menu Options)

| Code | Description                         |
|------|-------------------------------------|
| 1    | Select two tiles                    |
| 2    | Reveal one tile                     |
| 3    | Surrender – Show solution           |
| 4    | Start a new game                    |
| 5    | Quit                                |

---

## 🧱 Object-Oriented Concepts Used

- **Class-Based Design**: The grid and its behavior are encapsulated in a custom class.
- **Encapsulation**: Data related to the grid and gameplay is kept private within the class.
- **Modular Design**: Logic is divided across `game.py` and `grid.py` for clarity and separation of concerns.
- **Built-In Libraries**:
  - `os` (for screen clearing)
  - `time` (for timed reveals)
  - `random` (for number shuffling)
  - `sys` (for command-line arguments)
  - `string` (for input checks)

---

## 📊 Sample Outputs

Gameplay includes:
- Revealing matching or mismatching pairs
- Grid refresh and feedback on invalid inputs
- End-game score display based on this formula:

---

## 🛠 Technologies

- Language: Python 
- IDE: VS Code / PyCharm 
- Platform: Docker container
