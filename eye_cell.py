from cell import Cell
from cell_search import CellSearch

class EyeCell(Cell):
    def digest(self, food_cells):
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        distances = [
            CellSearch(food_cells, self.x, self.y, dx, dy).nearest_cell_distance()
            for dx, dy in directions
        ]
        return "".join(distances)
