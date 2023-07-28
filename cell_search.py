class CellSearch:
    def __init__(self, cells, origin_x, origin_y, direction, max_distance, is_vertical):
        self.cells = cells
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.direction = direction
        self.max_distance = max_distance
        self.is_vertical = is_vertical

    def nearest_cell(self):
        for i in range(self.origin_y, self.origin_y + self.direction * self.max_distance, self.direction):
            for cell in self.cells:
                if self.is_match(cell, i):
                    return cell
        return None

    def is_match(self, cell, i):
        return (cell.y == i and cell.x == self.origin_x) if self.is_vertical else (cell.x == i and cell.y == self.origin_x)
