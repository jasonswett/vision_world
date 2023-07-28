MAX_DISTANCE_TO_LOOK = 10

class CellSearch:
    def __init__(self, cells, origin_x, origin_y, direction, is_vertical):
        self.cells = cells
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.direction = direction
        self.is_vertical = is_vertical

    def nearest_cell(self):
        for i in range(self.origin_y, self.origin_y + self.direction * MAX_DISTANCE_TO_LOOK, self.direction):
            for cell in self.cells:
                if self.is_match(cell, i):
                    return cell
        return None

    def is_match(self, cell, i):
        return (cell.y == i and cell.x == self.origin_x) if self.is_vertical else (cell.x == i and cell.y == self.origin_x)
