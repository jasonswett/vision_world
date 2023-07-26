class Cell:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def occupies_same_space_as(self, other_cell):
        return self.x == other_cell.x and self.y == other_cell.y

    def adjacent_to(self, other_cell):
        x_distance = abs(other_cell.x - self.x)
        y_distance = abs(other_cell.y - self.y)
        if x_distance != 0 and y_distance != 0:
            return False
        if x_distance == 0 and y_distance == 0:
            return False
        return x_distance <= 1 and y_distance <= 1

    def move(self, dx, dy):
            self.x += dx
            self.y += dy
