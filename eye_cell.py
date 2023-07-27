from cell import Cell

MAX_DISTANCE_TO_LOOK = 100

class EyeCell(Cell):
    def north_color(self, cells):
        nearest_cell_up = self.nearest_cell_vertical(cells, direction=-1)
        return nearest_cell_up.color if nearest_cell_up else None

    def south_color(self, cells):
        nearest_cell_down = self.nearest_cell_vertical(cells, direction=1)
        return nearest_cell_down.color if nearest_cell_down else None

    def east_color(self, cells):
        nearest_cell_right = self.nearest_cell_horizontal(cells, direction=1)
        return nearest_cell_right.color if nearest_cell_right else None

    def west_color(self, cells):
        nearest_cell_left = self.nearest_cell_horizontal(cells, direction=-1)
        return nearest_cell_left.color if nearest_cell_left else None

    def nearest_cell_vertical(self, cells, direction):
        for y in range(self.y, self.y + direction * MAX_DISTANCE_TO_LOOK, direction):
            for cell in cells:
                if cell.x == self.x and cell.y == y:
                    return cell
        return None

    def nearest_cell_horizontal(self, cells, direction):
        for x in range(self.x, self.x + direction * MAX_DISTANCE_TO_LOOK, direction):
            for cell in cells:
                if cell.y == self.y and cell.x == x:
                    return cell
        return None

    def digest(self, cells):
        total = 0
        if self.nearest_cell_vertical(cells, direction=-1):
            total += 1
        if self.nearest_cell_horizontal(cells, direction=1):
            total += 2
        if self.nearest_cell_vertical(cells, direction=1):
            total += 3
        if self.nearest_cell_horizontal(cells, direction=-1):
            total += 4
        return total
