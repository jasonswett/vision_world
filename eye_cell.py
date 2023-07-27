from cell import Cell
from cell_search import CellSearch

MAX_DISTANCE_TO_LOOK = 100

class EyeCell(Cell):
    def digest(self, cells):
        total = 0
        if CellSearch(cells, self.x, self.y, -1, MAX_DISTANCE_TO_LOOK, True).nearest_cell():
            total += 1
        if CellSearch(cells, self.y, self.x, 1, MAX_DISTANCE_TO_LOOK, False).nearest_cell():
            total += 2
        if CellSearch(cells, self.x, self.y, 1, MAX_DISTANCE_TO_LOOK, True).nearest_cell():
            total += 3
        if CellSearch(cells, self.y, self.x, -1, MAX_DISTANCE_TO_LOOK, False).nearest_cell():
            total += 4
        return total
