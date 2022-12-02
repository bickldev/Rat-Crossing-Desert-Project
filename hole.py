import random
from cell import Cell

class Hole(Cell):
    hole_archive = []

    def __init__(self, coordinates):
        self.hole_archive.append(coordinates)
        self.cell_type = "H"

    def get_cell_type(self):
        return self.cell_type

    def move(self, current_rat):
        self.current_rat = current_rat
        result = random.choice(self.hole_archive)
        return result