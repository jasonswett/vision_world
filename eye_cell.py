from cell import Cell

MAX_DISTANCE_TO_LOOK = 100

class EyeCell(Cell):
    def north_color(self, cells):
        nearest_cell_up = self.nearest_cell_vertical(cells, direction=-1)
        return nearest_cell_up.color if nearest_cell_up else None

    def south_color(self, cells):
        nearest_cell_down = self.nearest_cell_vertical(cells, direction=1)
        return nearest_cell_down.color if nearest_cell_down else None

    def nearest_cell_vertical(self, cells, direction):
        for y in range(self.y, self.y + direction * MAX_DISTANCE_TO_LOOK, direction):
            for cell in cells:
                if cell.x == self.x and cell.y == y:
                    return cell
        return None
