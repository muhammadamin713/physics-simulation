import pygame
from vector2 import Vector2
from physics_obj import Physics2DObject

class Ball(Physics2DObject):
    def __init__(self, window, pos: Vector2, radius: int):
        super().__init__(pos)
        self.window = window
        self.radius = radius

    def update(self, dt):
        self.gravity(dt)
        self.pos.y = self.pos.clamp_y(self.radius, self.window.get_height() - self.radius)

        # -- Bouncing? --
        if self.pos.y >= self.window.get_height() - self.radius:
            self.velocity.y = -1 * self.velocity.y

    def render(self, surface, color, width=0):
        pygame.draw.circle(surface, color, self.pos.to_tuple(), self.radius, width=width)
