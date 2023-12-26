class CellSearch:
    MAX_DISTANCE_TO_LOOK = 100

    def __init__(self, food_cells, origin_x, origin_y, x_direction, y_direction):
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.x_direction = x_direction
        self.y_direction = y_direction
        self.food_cells = self._filter_relevant_cells(food_cells)

    def _filter_relevant_cells(self, food_cells):
        # Keep only cells where either x matches origin_x or y matches origin_y
        return [cell for cell in food_cells if cell.x == self.origin_x or cell.y == self.origin_y]

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
