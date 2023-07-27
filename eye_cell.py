from cell import Cell

MAX_DISTANCE_TO_LOOK = 100

class EyeCell(Cell):
    def north_color(self, cells):
        nearest_cell_up = self.nearest_cell_up(cells)
        return nearest_cell_up.color if nearest_cell_up else None

    def nearest_cell_up(self, cells):
            for y in range(self.y, self.y - MAX_DISTANCE_TO_LOOK, -1):
                for cell in cells:
                    if cell.x == self.x and cell.y == y:
                        return cell
            return None
