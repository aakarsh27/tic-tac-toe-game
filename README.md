# TIC-TAC-TOE GAME in python

### 1. `ai-player.py`

`ai-player.py` is a Python script implementing a classic Tic Tac Toe game for two players. The game is played on a 3x3 grid where players take turns placing their marks (X or O) in empty cells. The script handles player input validation, checks for win conditions, and displays the game board after each move. The game continues until a player wins or the board is full, resulting in a draw.

### 2. `single-player.py`

`single-player.py` is a Python script that provides an AI opponent for playing against a human player in Tic Tac Toe. The AI opponent uses a basic strategy to make moves:
- It attempts to win the game by placing its mark in a winning position if available.
- If it cannot win in the current move, it checks to block the human player from winning by placing its mark strategically.
- If no immediate win or block is possible, it places its mark in the center if available; otherwise, it chooses a random empty cell.

The AI opponent's strategy ensures a challenging game against a human player, making decisions based on simple rules to prioritize winning or preventing the opponent's victory. Players can interactively play against this AI opponent to test their skills in Tic Tac Toe.
