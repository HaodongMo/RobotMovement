# Simulation of a robot toy moving about a table
# Commands which would cause the robot to fall off the table will be blocked.
# The commands are:

# PLACE X,Y,F
#  where X,Y are the coordinates and F is the direction (NORTH, SOUTH, EAST, WEST) the robot is facing
#  this must be the first command. Commands are to be discarded until a valid PLACE command is executed.
# MOVE
# LEFT
# RIGHT
# REPORT

FACING = ['NORTH', 'EAST', 'SOUTH', 'WEST']
DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class robot():
    x: 0
    y: 0
    facing: 0
    # 0 = North, 1 = East, 2 = South, 3 = West
    placed: False
    fallen: False

    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.placed = True
        self.facing = FACING.index(dir)
        self.fallen = False

    def move(self):
        if self.fallen:
            print("Robot has fallen off the table and cannot move.")
            return

        if self.placed:
            self.x += DIR[self.facing][0]
            self.y += DIR[self.facing][1]

        # check if robot is still on the table
        if self.x < 0 or self.x > 5 or self.y < 0 or self.y > 5:
            print("Robot fell off the table!")
            self.fallen = True

    def left(self):
        if self.fallen:
            print("Robot has fallen off the table and cannot turn.")
            return

        if self.placed:
            self.facing = (self.facing - 1) % 4

    def right(self):
        if self.fallen:
            print("Robot has fallen off the table and cannot turn.")
            return

        if self.placed:
            self.facing = (self.facing + 1) % 4

    def report(self):
        if self.placed:
            print("Output: ", end="")
            print(self.x, self.y, FACING[self.facing], sep=",")

            if self.fallen:
                print("Robot is off the table.")


def runrobot(filename):
    # Load commands from file
    with open(filename, "r") as f:
        commands = f.readlines()

        r = None
        
        for command in commands:
            command = command.strip().upper()
            print(command)

            if command.startswith("PLACE"):
                # get x, y and direction
                x, y, dir = command[6:].split(",")
                x = int(x)
                y = int(y)

                # check if robot is placed on the table
                if x < 0 or x > 5 or y < 0 or y > 5:
                    print("Robot cannot be placed off the table.")
                    continue

                # check if direction is valid
                if dir not in FACING:
                    print("Invalid direction.")
                    continue

                # place robot
                r = robot(x, y, dir)

            elif command.startswith("#"):
                # Comment
                pass

            elif command == "MOVE":
                if r:
                    r.move()

            elif command == "LEFT":
                if r:
                    r.left()

            elif command == "RIGHT":
                if r:
                    r.right()

            elif command == "REPORT":
                if r:
                    r.report()

            else:
                print("Invalid command.")

# run runrobot() on all files in current directory beginning with "test" and ending in ".txt"

import os

for file in os.listdir():
    if file.startswith("test") and file.endswith(".txt"):
        print(file, ") ----------------", sep="")
        runrobot(file)
        print()