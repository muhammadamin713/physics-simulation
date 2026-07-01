import pygame
from vector2 import Vector2

class Physics2DObject:
    GRAVITY = 9.81

    def __init__(self, pos: Vector2):
        self.pos = pos
        self.speed = 0

    def gravity(self, dt):
        """
        This function only implement gravity without considering
        the landing platform. You need to clamp the value of pos.y
        yourself.
        """
        self.accel(self.GRAVITY)
        self.pos.y += self.speed * dt

    def accel(self, value):
        self.speed += value
