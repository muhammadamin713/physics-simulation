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
