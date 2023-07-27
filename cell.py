class Cell:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def move_to(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]

    def coordinates(self):
        return (self.x, self.y)
