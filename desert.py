import random
from cell_interface import CellInterface
from hole import Hole
from cell import Cell
from rat import Rat

class Desert:
    rat_counter = 0
    rat_location = [0,0]

    def __init__(self, size_of_desert):
        self.rows = size_of_desert[0]
        self.columns = size_of_desert[1]

        self.desert = [[CellInterface() for rows in range(self.rows)] for columns in range(self.columns)]
        self.desert = self.create_cells(self.rows, self.columns)

    def create_cells(self, rows, columns):
        for row in range(rows):
            for column in range(columns):
                cell_type = self.determine_cell_type()

                if cell_type == "C":
                    self.desert[row][column] = Cell([row, column])
                else:
                    self.desert[row][column] = Hole([row, column])
        return self.desert

    def determine_cell_type(self):
        self.possible_cell_types = ["C", "C", "C", "C", "C", "C", "C", "C", "C", "H"]
        cell_type = random.choice(self.possible_cell_types)

        return cell_type

    def get_cell_type(self, coordinates):

        return self.desert[coordinates[0]][coordinates[1]].get_cell_type()

    def start_rat(self):
        self.rat_counter += 1
        self.current_rat = Rat("Rat" + str(self.rat_counter))
        self.rat_location = [0,0]

    def move_rat(self):
        
        while self.current_rat.alive_status != -1:
            if self.current_rat.alive_status != 0:
                self.start_rat()

            self.move_x = random.choice(range(2))
            self.move_y = random.choice(range(2))

            if (self.rat_location[0] + self.move_x >= 0) and (self.rat_location[0] + self.move_x < self.rows):
                if (self.rat_location[1] + self.move_y >= 0) and (self.rat_location[1] + self.move_y < self.columns):
                    self.rat_location[0] += self.move_x
                    self.rat_location[1] += self.move_y
            
            self.rat_location = self.desert[self.rat_location[0]][self.rat_location[1]].move(self.current_rat)

            if self.current_rat.exhaustion_rate >= 6:
                self.current_rat.set_alive_status(1)
            
            self.current_rat.add_rat_location_archive((self.rat_location[0], self.rat_location[1]))

            if (self.rat_location[0] == self.rows - 1) and (self.rat_location[1] == self.columns - 1):
                self.current_rat.set_alive_status(-1)

        print(str(self.current_rat.ratID) + " made it!")
        print("Here is the path that the rat took:")
        for i in range(len(self.current_rat.get_rat_location_archive())):
            print(self.current_rat.get_rat_location_archive()[i], end=" ")