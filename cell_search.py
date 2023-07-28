MAX_DISTANCE_TO_LOOK = 10

class CellSearch:
    def __init__(self, food_cells, origin_x, origin_y, x_direction, y_direction):
        self.food_cells = food_cells
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.x_direction = x_direction
        self.y_direction = y_direction

    def nearest_cell(self):
        x = self.origin_x
        y = self.origin_y

        for distance in range(MAX_DISTANCE_TO_LOOK):
            x += self.x_direction
            y += self.y_direction

            matching_cell = self._cell_at_coordinates(x, y)
            if matching_cell is not None:
                return matching_cell

        return None

    def _cell_at_coordinates(self, x, y):
        for food_cell in self.food_cells:
            if food_cell.x == x and food_cell.y == y:
                return food_cell
        return None
