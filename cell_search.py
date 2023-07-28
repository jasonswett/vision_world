MAX_DISTANCE_TO_LOOK = 10

class CellSearch:
    def __init__(self, cells, origin_x, origin_y, x_direction, y_direction):
        self.cells = cells
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.x_direction = x_direction
        self.y_direction = y_direction

    def nearest_cell(self):
        x_range = range(self.origin_x, self.origin_x + self.x_direction * MAX_DISTANCE_TO_LOOK, self.x_direction or 1)
        y_range = range(self.origin_y, self.origin_y + self.y_direction * MAX_DISTANCE_TO_LOOK, self.y_direction or 1)

        for i in x_range:
            for j in y_range:
                for cell in self.cells:
                    if self.is_match(cell, i, j):
                        return cell
        return None

    def is_match(self, cell, i, j):
        return cell.x == i and cell.y == j
