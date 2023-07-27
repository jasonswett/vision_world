from cell import Cell
from cell_search import CellSearch

MAX_DISTANCE_TO_LOOK = 100

class EyeCell(Cell):
    def up_color(self, cells):
        nearest_cell_up = self.nearest_cell_vertical(cells, direction=-1)
        return nearest_cell_up.color if nearest_cell_up else None

    def down_color(self, cells):
        nearest_cell_down = self.nearest_cell_vertical(cells, direction=1)
        return nearest_cell_down.color if nearest_cell_down else None

    def right_color(self, cells):
        nearest_cell_right = self.nearest_cell_horizontal(cells, direction=1)
        return nearest_cell_right.color if nearest_cell_right else None

    def left_color(self, cells):
        nearest_cell_left = self.nearest_cell_horizontal(cells, direction=-1)
        return nearest_cell_left.color if nearest_cell_left else None

    def nearest_cell_vertical(self, cells, direction):
        search = CellSearch(cells, self.x, self.y, direction, MAX_DISTANCE_TO_LOOK, True)
        return search.nearest_cell()

    def nearest_cell_horizontal(self, cells, direction):
        search = CellSearch(cells, self.y, self.x, direction, MAX_DISTANCE_TO_LOOK, False)
        return search.nearest_cell()

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
