import pygame
from vector2 import Vector2

class Physics2DObject:
    GRAVITY = 9.81

    def __init__(self, pos: Vector2):
        self.pos = pos
        self.velocity = Vector2(0, 0)

    def gravity(self, dt):
        """
        This function only implement gravity without considering
        the landing platform. You need to clamp the value of pos.y
        yourself.
        """
        self.velocity.y += self.GRAVITY
        self.pos.y += self.velocity.y * dt
    
    def debug_direction(self, surface, color="blue", line_scale=0.25):
        dir = self.velocity.normalize().scale(self.velocity.length() * line_scale)
        pygame.draw.line(surface, color,
                         self.pos.to_tuple(),
                         (self.pos + dir).to_tuple()
                         )
