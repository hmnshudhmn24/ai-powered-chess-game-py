import chess
import chess.engine
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
SQUARE_SIZE = WIDTH // 8
WHITE, BLACK = (238, 238, 210), (118, 150, 86)

# Load Stockfish engine (Download and specify the correct path)
STOCKFISH_PATH = "stockfish/stockfish.exe"  # Change this path
engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

# Initialize board
board = chess.Board()

# Pygame window setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Chess Game")

# Load images
piece_images = {}
for piece in chess.PIECE_SYMBOLS[1:]:
    piece_images[f'w{piece}'] = pygame.image.load(f'assets/w{piece}.png')
    piece_images[f'b{piece}'] = pygame.image.load(f'assets/b{piece}.png')

def draw_board():
    """Draws the chess board."""
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces():
    """Draws the chess pieces on the board."""
    for row in range(8):
        for col in range(8):
            piece = board.piece_at(chess.square(col, 7 - row))
            if piece:
                img = piece_images[f'{"w" if piece.color else "b"}{piece.symbol()}']
                screen.blit(pygame.transform.scale(img, (SQUARE_SIZE, SQUARE_SIZE)), (col * SQUARE_SIZE, row * SQUARE_SIZE))

def ai_move():
    """Handles the AI's move."""
    if not board.is_game_over():
        result = engine.play(board, chess.engine.Limit(time=0.5))
        board.push(result.move)

def get_square(pos):
    """Gets the board square from screen coordinates."""
    x, y = pos
    return chess.square(x // SQUARE_SIZE, 7 - (y // SQUARE_SIZE))

def main():
    running = True
    selected_square = None
    player_turn = True  # White moves first

    while running:
        draw_board()
        draw_pieces()
        pygame.display.flip()

        if not player_turn:
            ai_move()
            player_turn = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN and player_turn:
                square = get_square(event.pos)
                if selected_square is None:
                    if board.piece_at(square) and board.piece_at(square).color == chess.WHITE:
                        selected_square = square
                else:
                    move = chess.Move(selected_square, square)
                    if move in board.legal_moves:
                        board.push(move)
                        player_turn = False
                    selected_square = None

    pygame.quit()
    engine.quit()
    sys.exit()

if __name__ == "__main__":
    main()
