from cell import Cell
from cell_search import CellSearch

class EyeCell(Cell):
    def digest(self, food_cells):
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        findings = [CellSearch(food_cells, self.x, self.y, dx, dy).nearest_cell() for dx, dy in directions]
        return "".join(["1" if finding else "0" for finding in findings])
