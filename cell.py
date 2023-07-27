class Cell:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def move(self, dx, dy):
            self.x += dx
            self.y += dy
