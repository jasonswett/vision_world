class Ecosystem:
    def eatable_food_cell(self, organism, food_cells):
        for cell in organism.cells:
            for food_cell in food_cells:
                if food_cell.x == cell.x and food_cell.y == cell.y:
                    return food_cell
        return None
