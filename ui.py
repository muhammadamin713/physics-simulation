import pygame

class Label:
    def __init__(self, window, pos, text, font_px=30):
        self.window = window
        self.pos = pos
        self.text = text
        self.font = pygame.Font(None, font_px)

    def set_text(self, text):
        self.text = text

    def set_pos(self, x, y):
        self.pos = (x, y)

    def get_font(self):
        return self.font

    def render(self, color, antialias=False):
        self.label_surface = self.font.render(self.text, antialias, color)
        self.window.blit(self.label_surface, dest=self.pos)
