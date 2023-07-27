class CellSearch:
    def __init__(self, cells, fixed_coord, start, direction, max_distance, is_vertical):
        self.cells = cells
        self.fixed_coord = fixed_coord
        self.start = start
        self.direction = direction
        self.max_distance = max_distance
        self.is_vertical = is_vertical

    def nearest_cell(self):
        for i in range(self.start, self.start + self.direction * self.max_distance, self.direction):
            for cell in self.cells:
                if self.is_match(cell, i):
                    return cell
        return None

    def is_match(self, cell, i):
        return (cell.y == i and cell.x == self.fixed_coord) if self.is_vertical else (cell.x == i and cell.y == self.fixed_coord)
