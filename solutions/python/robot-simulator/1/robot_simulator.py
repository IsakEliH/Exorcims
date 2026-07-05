# Globals for the directions
# Change the values as you see fit
EAST = "EAST"
NORTH = "NORTH"
WEST = "WEST"
SOUTH = "SOUTH"

DIR_LIST: list = [WEST, NORTH, EAST, SOUTH]

MOVEMENT: dict = {EAST: (1, 0), NORTH: (0, 1), WEST: (-1, 0), SOUTH: (0, -1)}


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.coordinates: tuple = (x_pos, y_pos)
        self.direction = direction
        self.index = DIR_LIST.index(direction)

    def move(self, dir_str: str):
        for letter in dir_str:
            movement: list[str] = ["A", "R", "L"]
            if letter not in movement:
                return None

            if letter == "R":
                self.index += 1
            elif letter == "L":
                self.index -= 1
            elif letter == "A":
                add: tuple = MOVEMENT[DIR_LIST[self.index % 4]]

                self.coordinates = (
                    self.coordinates[0] + add[0],
                    self.coordinates[1] + add[1],
                )
        self.direction = DIR_LIST[self.index % 4]
        return self.direction
