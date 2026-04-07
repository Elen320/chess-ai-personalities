import pygame # for interface
import chess # chess logic, identifies legal moves
import sys
import random


pygame.init()

screen = pygame.display.set_mode((720, 720))

pygame.display.set_caption("Chess with personalities")

running = True

Light_color = (218, 224, 215)
Dark_color = (72, 105, 56)
Offset = (720-80*8)//2

# Load piece images
piece_images = {}
piece_names = {
    'P': 'wp', 'N': 'wn', 'B': 'wb', 'R': 'wr', 'Q': 'wq', 'K': 'wk',
    'p': 'bp', 'n': 'bn', 'b': 'bb', 'r': 'br', 'q': 'bq', 'k': 'bk'
}
for symbol, name in piece_names.items():
    piece_images[symbol] = pygame.image.load(f'assets/{name}.png')

# Create chess board
board = chess.Board()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((58, 66, 57))
    for row in range(8):
        for col in range(8):
            is_light_square = (row+col)%2 == 0
            color = Light_color if is_light_square else Dark_color
            pygame.draw.rect(screen, color, pygame.Rect(Offset +col*80, Offset + row*80, 80, 80))
            
            # Draw pieces
            square = chess.square(col, 7-row)  # Convert to chess square (0=a1, 7=h1, 56=a8, etc.)
            piece = board.piece_at(square)
            if piece:
                symbol = piece.symbol()
                if symbol in piece_images:
                    screen.blit(piece_images[symbol], (Offset + col*80, Offset + row*80))
    
    pygame.display.flip()
pygame.quit()
sys.exit()