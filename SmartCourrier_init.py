import turtle as ttl
from enum import Enum

class Courrier(ttl.Turtle):
    _ahead = None
    
    class Direction(Enum):
        NORTH = 1
        SOUTH = 2
        WEST = 3
        EAST = 4

    def __init__(self):
        ttl.Turtle.__init__(self)
        self.shape()
        self.shapesize(1.5, 1.5)
    
    def goFoward(self):
        pass
    
    def turnRight(self):
        self.right(90)
    
    def turnLeft(self):
        self.left(90)
    
    def checkFront(self):
        pass
    
    def searchDestination():
        pass

class Street(ttl.Turtle):
    def __init__(self):
        ttl.Turtle.__init__(self)
        self.shape()

class Ruko(ttl.Turtle):
    def __init__(self):
        ttl.Turtle.__init__(self)
        self.shape()

class Destination(ttl.Turtle):
    def __init__(self):
        ttl.Turtle.__init__(self)
        self.shape()

def createStreetArray(row, col):
    street = []
    return street

# Main Program
win = ttl.Screen()
win.title("Smart Courrier")
win.setup(1280, 720)

# 1. Siapkan kurir, jalan, dan bangunan
kurir = Courrier()

kurir.turnLeft()
kurir.turnRight()

# 2. Buat list jalur, dan slkdjfsdfffffc vjsc
jalur = []
jalan = [[]]
