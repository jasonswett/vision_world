class CellSearch:
    MAX_DISTANCE_TO_LOOK = 8

    def __init__(self, food_cells, origin_x, origin_y, x_direction, y_direction):
        self.food_cells = food_cells
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.x_direction = x_direction
        self.y_direction = y_direction

    def nearest_cell_distance(self):
        x = self.origin_x
        y = self.origin_y

        for distance in range(self.MAX_DISTANCE_TO_LOOK):
            x += self.x_direction
            y += self.y_direction

            if self._cell_at_coordinates(x, y) is not None:
                if distance < 0.2 * self.MAX_DISTANCE_TO_LOOK:
                    return '01'
                elif distance < 0.5 * self.MAX_DISTANCE_TO_LOOK:
                    return '10'
                else:
                    return '11'

        return '00'

    def _cell_at_coordinates(self, x, y):
        for food_cell in self.food_cells:
            if food_cell.x == x and food_cell.y == y:
                return food_cell
        return None
