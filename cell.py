import random
from cell_interface import CellInterface
from rat import Rat

class Cell(CellInterface):

    cell_type = "C"
    possible_cell_types = ["C", "S", "W"]

    def __init__(self, coordinates):
        self.cell_type = random.choice(self.possible_cell_types)
        self.x = coordinates[0]
        self.y = coordinates[1]

    def get_cell_type(self):
        return self.cell_type

    def move(self, current_rat):

        self.current_rat = current_rat

        match self.cell_type:
            case "C":
                if self.randomize():
                    self.current_rat.exhaust()
                else:
                    self.current_rat.refresh()
            case "S":
                self.current_rat.refresh()
            case "W":
                self.current_rat.exhaust()

        return [self.x, self.y]

    def randomize(self):
        result = random.choice(range(2))
        return result