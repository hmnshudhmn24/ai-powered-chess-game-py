# AI-Powered Chess Game

## Overview
This is a Python-based AI-powered chess game with a graphical user interface (GUI) built using Pygame. The AI opponent is powered by the Stockfish chess engine, providing strong gameplay.

## Features
- Graphical chessboard using Pygame
- Player vs. AI mode (Stockfish AI)
- Move validation and legal move enforcement
- Automatic AI move handling

## Requirements
- Python 3.8+
- Pygame
- Python-Chess
- Stockfish Chess Engine

## Installation
1. Install the required dependencies:
```sh
pip install pygame chess
```
2. Download the Stockfish engine from [Stockfish Website](https://stockfishchess.org/download/).
3. Update the `STOCKFISH_PATH` in the script to point to your Stockfish executable.

## Running the Game
Run the following command:
```sh
python ai_chess_game.py
```

## How to Play
- The game starts with White (Player) vs. AI (Black).
- Click on a piece to select it and then click on a valid square to move.
- The AI will automatically make a move after the player moves.

## License
This project is open-source and free to use.
