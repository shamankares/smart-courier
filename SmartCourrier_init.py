import turtle as ttl
import random as rand
from enum import Enum

class Direction(Enum):
        NORTH = 1
        SOUTH = 2
        WEST = 3
        EAST = 4

class Courrier(ttl.Turtle):
    def __init__(self, direction=None):
        ttl.Turtle.__init__(self)
        self._ahead = direction
        self.shape()
        self.shapesize(1.5, 1.5)
    
    def goFoward(self):
        '''
        Jika hadap utara:
            pindah ke atas
        Jika hadap selatan:
            pindah ke bawah
        Jika hadap barat:
            pindah ke kiri
        Jika hadap timur:
            pindah ke kanan
        '''
        pass
    
    def turnRight(self):
        self.right(90)
    
    def turnLeft(self):
        self.left(90)
    
    def turn(self, current, next):
        difference = (next[0] - current[0], next[0] - current[0])
        '''
        Jika jalur ke bawah:
            dan hadap ke timur:
                belokKanan()
            atau hadap ke barat:
                belokKiri()
        jika jalur ke atas:
            dan hadap ke timur:
                belokKiri()
            atau hadap ke barat:
                belokKanan()
        jika jalur ke kanan:
            dan hadap ke utara:
                belokKiri()
            atau hadap ke selatan:
                belokKanan()
        jika jalur ke kiri:
        jika jalur berlawanan:

        '''
        pass
    
    def searchDestination():
        pass

    def go():
        '''
        Jika sampai pada tujuan
        '''
        pass

class Street(ttl.Turtle):
    def __init__(self):
        ttl.Turtle.__init__(self)
        self.shape("square")

class Ruko(ttl.Turtle):
    def __init__(self):
        ttl.Turtle.__init__(self)
        self.shape("square")

class Destination(ttl.Turtle):
    def __init__(self, position=None):
        ttl.Turtle.__init__(self)
        self.shape("triangle")
        self.position = position
        self.area = (   (position[0], position[1] + 1),
                        (position[0], position[1] - 1),
                        (position[0] + 1, position[1]),
                        (position[0] - 1, position[1]), )

def createMaze(row, col):
    street = []
    for x in range(row):
        street_row = []
        for y in range(col):
            num = rand.random()
            if num < 0.35:
                street_row.append('b')
            else:
                street_row.append('s')
        street.append(street_row)
    return street

def main():
    # Main Program
    win = ttl.Screen()
    win.title("Smart Courrier")
    win.setup(1280, 720)

    # 1. Siapkan kurir, jalan, dan bangunan
    kurir = Courrier()

    kurir.turnLeft() ### debug
    kurir.turnRight() ### debug

    # 2. Buat list jalur, dan slkdjfsdfffffc vjsc
    jalur = []
    maze = createMaze(20, 20)
    for i in maze:
        print(i)

if __name__ == '__main__':
    main()