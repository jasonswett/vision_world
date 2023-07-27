from eye_cell import EyeCell

class Organism:
    def __init__(self, x, y):
        self.cells = [EyeCell(x, y, (255, 0, 0))]

    def move(self, dx, dy):
        for cell in self.cells:
            cell.move(dx, dy)
