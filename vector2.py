import math

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clamp_y(self, mini, maxi):
        if self.y > maxi:
            return maxi
        if self.y < mini:
            return mini
        return self.y

    def to_tuple(self):
        return (self.x, self.y)

    def normalize(self):
        length = self.length()
        return Vector2(self.x / length, self.y / length)

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def scale(self, value):
        return Vector2(self.x * value, self.y * value)

    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f})"

    def __add__(self, vector2):
        return Vector2(self.x + vector2.x, self.y + vector2.y)

    def __sub__(self, vector2):
        return Vector2(self.x - vector2.x, self.y - vector2.y)
