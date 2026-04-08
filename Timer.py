import pygame

class ChessTimer:
    def __init__(self, total_seconds, font_color=(255, 255, 255)):
        self.time_left = total_seconds
        self.font = pygame.font.SysFont("Arial", 32, bold = True)
        self.color = font_color
    
    def update(self, dt):
        if self.time_left > 0:
            self.time_left -= dt
        else:
            self.time_left = 0
            
    def draw(self, screen, x, y):
        minutes = int(self.time_left // 60)
        seconds = int(self.time_left % 60)
        time_str = f"{minutes:02d}:{seconds:02d}"
        text_surface = self.font.render(time_str, True, self.color)
        screen.blit(text_surface, (x, y))