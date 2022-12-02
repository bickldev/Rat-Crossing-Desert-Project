class Rat:
    alive_status = 0 #-1 is made it, 0 is alive, 1 is lost/dead
    ratID = "null"
    exhaustion_rate = 0

    def __init__(self, ratID):
        self.ratID = ratID
        self.rat_location_archive = [(0, 0)]

    def set_alive_status(self, alive_status):
        self.alive_status = alive_status

    def add_rat_location_archive(self, coordinates):
        self.rat_location_archive.append(coordinates)

    def get_rat_location_archive(self):
        return self.rat_location_archive

    def exhaust(self):
        self.exhaustion_rate += 1

    def refresh(self):
        if self.exhaustion_rate > 0:
            self.exhaustion_rate -= 1